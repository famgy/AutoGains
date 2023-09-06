import win32gui
import win32con
import re

WINDOW_ID = 0


def get_window_titles():
    def callback(hwnd, extra):
        window_text = win32gui.GetWindowText(hwnd)
        if window_text:
            print(window_text)
            extra.append(window_text)

    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows


def locate_window(name):
    global WINDOW_ID
    WINDOW_ID = win32gui.FindWindow(None, name)

    if WINDOW_ID != 0:
        return WINDOW_ID

    def callback(wid, pattern):
        global WINDOW_ID

        if re.match(pattern, str(win32gui.GetWindowText(wid))) is not None:
            WINDOW_ID = wid

    win32gui.EnumWindows(callback, name)

    return WINDOW_ID


def is_window_focused( window_id):
    focused_window_id = win32gui.GetForegroundWindow()
    return focused_window_id == window_id


def get_focused_window_name():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())


def bring_window_to_top(window_id):
    win32gui.ShowWindow(window_id, win32con.SW_RESTORE)
    win32gui.SetWindowPos(window_id, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(window_id, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(window_id, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)


def focus_window(window_id):
    win32gui.SetForegroundWindow(window_id)


def get_window_geometry(window_id):
    geometry = dict()

    x, y, width, height = win32gui.GetClientRect(window_id)

    geometry["width"] = width
    geometry["height"] = height

    x0, y0, x1, y1 = win32gui.GetWindowRect(window_id)

    border_width = ((x1 - x0 - width) // 2)

    geometry["x_offset"] = x0 + border_width
    geometry["y_offset"] = y0 + (y1 - y0 - height - border_width)

    return geometry
