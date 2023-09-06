
import win32gui


def get_window_titles():
    def callback(hwnd, extra):
        window_text = win32gui.GetWindowText(hwnd)
        if window_text:
            extra.append(window_text)

    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows
