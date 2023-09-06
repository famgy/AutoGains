import os

import mss
import mss.tools

current_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(current_dir, "images")


class FrameGrabber:
    def __init__(self, window_geometry=None):
        if window_geometry is None:
            raise ValueError("window_geometry must be provided.")

        self.width = window_geometry['width']
        self.height = window_geometry['height']

        self.x_offset = window_geometry['x_offset']
        self.y_offset = window_geometry['y_offset']

        self.screen_grabber = mss.mss()

    def start(self):
        while True:
            monitor = {"top": self.y_offset, "left": self.x_offset, "width": self.width, "height": self.height}
            output = "{}/frame-{}x{}_{}x{}.png".format(images_path,
                                                       monitor['top'],
                                                       monitor['left'],
                                                       monitor['width'],
                                                       monitor['height'])

            frame_img = self.screen_grabber.grab(monitor)
            mss.tools.to_png(frame_img.rgb, frame_img.size, output=output)

            break
