import os
import time

import mss
import mss.tools
import numpy as np
import skimage.io

from redis.client import StrictRedis

import window_controller
from game_frame import GameFrame

current_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(current_dir, "images")


class FrameGrabber:
    def __init__(self, window_id, window_geometry=None):
        self.window_id = window_id

        if window_geometry is None:
            raise ValueError("window_geometry must be provided.")

        self.width = window_geometry['width']
        self.height = window_geometry['height']

        self.x_offset = window_geometry['x_offset']
        self.y_offset = window_geometry['y_offset']

        self.screen_grabber = mss.mss()

        self.redis_client = StrictRedis(host='127.0.0.1', port=6379)

        self.fps = 30
        self.buffer_seconds = 5
        self.frame_time = 1 / self.fps
        self.frame_buffer_size = self.buffer_seconds * self.fps

        # Clear any previously stored frames
        self.redis_client.delete("SERPENT:FRAMES")

        self.game_frames = list()

    def start(self):
        while True:
            if not window_controller.is_window_focused(self.window_id):
                return

            cycle_start = time.time()

            frame = self.grab_frame()

            frame_shape = str(frame.shape).replace("(", "").replace(")", "")
            frame_dtype = str(frame.dtype)

            frame_bytes = f"{cycle_start}~{frame_shape}~{frame_dtype}~".encode("utf-8") + frame.tobytes()

            self.redis_client.lpush("SERPENT:FRAMES", frame_bytes)
            self.redis_client.ltrim("SERPENT:FRAMES", 0, self.frame_buffer_size)

            cycle_end = time.time()

            cycle_duration = (cycle_end - cycle_start)
            cycle_duration -= int(cycle_duration)

            frame_time_left = self.frame_time - cycle_duration

            if frame_time_left > 0:
                time.sleep(frame_time_left)

            list_size = self.redis_client.llen("SERPENT:FRAMES")
            if list_size > 50:
                break

            # monitor = {"top": self.y_offset, "left": self.x_offset, "width": self.width, "height": self.height}
            # output = "{}/frame-{}x{}_{}x{}.png".format(images_path,
            #                                            monitor['top'],
            #                                            monitor['left'],
            #                                            monitor['width'],
            #                                            monitor['height'])
            #
            # frame_img = self.screen_grabber.grab(monitor)
            # mss.tools.to_png(frame_img.rgb, frame_img.size, output=output)
            #
            # break

    def grab_frame(self):
        monitor = {"top": self.y_offset, "left": self.x_offset, "width": self.width, "height": self.height}
        screenshot = self.screen_grabber.grab(monitor)

        frame = np.array(screenshot.pixels, dtype=np.uint8)

        frame = frame[..., [2, 1, 0]]

        return frame

    def get_frames(self):
        try:
            list_elements = self.redis_client.lrange("SERPENT:FRAMES", 0, -1)
            for index, frame_data in enumerate(list_elements):
                timestamp, shape, dtype, frame_bytes = frame_data.split("~".encode("utf-8"), maxsplit=3)

                frame_shape = [int(i) for i in shape.decode("utf-8").split(", ")]
                frame_array = np.fromstring(frame_bytes, dtype=dtype.decode("utf-8")).reshape(frame_shape)

                game_frame = GameFrame(frame_array, timestamp=float(timestamp))
                self.game_frames = [game_frame] + self.game_frames
        except Exception as e:
            raise e

    def collect_frames_for_context(self, context):
        print(f'Start collect_frames_for_context')

        self.get_frames()

        if not os.path.isdir(f"datasets/collect_frames_for_context/{context}"):
            os.mkdir(f"datasets/collect_frames_for_context/{context}")

        for i, game_frame in enumerate(self.game_frames):
            file_name = f"datasets/collect_frames_for_context/{context}/frame_{game_frame.timestamp}.png"

            print(f"Saving image {i + 1}/{len(self.game_frames)} to disk...")
            skimage.io.imsave(file_name, game_frame.frame_array)

        # self.game_frames = list()
