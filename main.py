import os
import subprocess

# import win32gui
# import tensorflow as tf

current_dir = os.path.dirname(os.path.abspath(__file__))
python32_path = r'C:\Users\szgpf\anaconda3\envs\python32_env\python.exe'
script_path = os.path.join(current_dir, "dll32_cmd.py")
imags_folder = "images"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    i = 0
    while i < 30000:
        i = i + 1

        subprocess.run([python32_path, script_path, "key_ctl_tab"], capture_output=True, text=True)
        subprocess.run([python32_path, script_path, "mouse_move"], capture_output=True, text=True)
        subprocess.run([python32_path, script_path, "key_click"], capture_output=True, text=True)

        subprocess.run([python32_path, script_path, "sleep_random"], capture_output=True, text=True)


    # window_titles = get_window_titles()
    # for title in window_titles:
    #     print(title)

    # hWnd = win32gui.FindWindow(None, "PADM00")
    # left, top, right, bot = win32gui.GetWindowRect(hWnd)
    # width = right - left
    # height = bot - top
    #
    #
    # hello = tf.constant("Hello, Tensorflow!")
    # sess = tf.Session()


