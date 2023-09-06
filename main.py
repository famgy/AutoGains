
import win32gui
import tensorflow as tf

import window_controller
from frame_grabber import FrameGrabber
from teammate_round_bot import round_auto


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    # get_window_titles()

    window_id = window_controller.locate_window("Pixel 2")
    window_controller.bring_window_to_top(window_id)
    window_controller.focus_window(window_id)
    window_geometry = window_controller.get_window_geometry(window_id)

    # screen capture
    frame_grabber = FrameGrabber(window_geometry)
    frame_grabber.start()



    # round_auto()


    # hello = tf.constant("Hello, Tensorflow!")
    # sess = tf.Session()



