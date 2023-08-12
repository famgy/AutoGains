import ctypes
import os
import sys
import time

files_folder = "libs"  # 替换为实际的文件夹路径
lib_file = os.path.join(files_folder, "msdk.dll")


def key_ctl_tab():
    objdll = ctypes.windll.LoadLibrary(lib_file)
    hdl = objdll.M_Open(1)

    objdll.M_KeyDown(hdl, 224)
    objdll.M_KeyPress(hdl, 43, 1)
    time.sleep(0.05)
    objdll.M_KeyUp(hdl, 224)


def mouse_move():
    objdll = ctypes.windll.LoadLibrary(lib_file)
    hdl = objdll.M_Open(1)

    objdll.M_ResolutionUsed(hdl, 1920, 1080)
    objdll.M_MoveTo3(hdl, 1343, 680)
    objdll.M_DelayRandom(1 * 1000, 2 * 1000);


def key_click():
    objdll = ctypes.windll.LoadLibrary(lib_file)
    hdl = objdll.M_Open(1)

    objdll.M_LeftClick(hdl, 1);


def sleep_random():
    objdll = ctypes.windll.LoadLibrary(lib_file)

    objdll.M_DelayRandom(10*1000, 15*1000);


if __name__ == "__main__":
    result = ""

    # 获取父进程传递的函数参数
    function_arg = str(sys.argv[1])  # 假设参数是整数类型

    # 调用函数并获取返回结果
    if "key_ctl_tab" == function_arg:
        key_ctl_tab()
    elif "mouse_move" == function_arg:
        mouse_move()
    elif "key_click" == function_arg:
        key_click()
    elif "sleep_random" == function_arg:
        sleep_random()
    else:
        print("There is not function : " + function_arg)


    # 将结果返回给父进程
    print(result)