
import win32gui
import tensorflow as tf

from teammate_round_bot import round_auto
from win32_util import get_window_titles

imags_folder = "images"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    round_auto()

    # window_titles = get_window_titles()
    # for title in window_titles:
    #     print(title)
    #
    # hWnd = win32gui.FindWindow(None, "PADM00")
    # left, top, right, bot = win32gui.GetWindowRect(hWnd)
    # width = right - left
    # height = bot - top
    #
    # hello = tf.constant("Hello, Tensorflow!")
    # sess = tf.Session()



