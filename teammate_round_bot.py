import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(current_dir, "dll32_cmd.py")
python32_path = r'C:\Users\szgpf\anaconda3\envs\python32_env\python.exe'


def round_auto():
    i = 0
    while i < 30000:
        i = i + 1

        subprocess.run([python32_path, script_path, "key_ctl_tab"], capture_output=True, text=True)
        subprocess.run([python32_path, script_path, "mouse_move"], capture_output=True, text=True)
        subprocess.run([python32_path, script_path, "key_click"], capture_output=True, text=True)

        subprocess.run([python32_path, script_path, "sleep_random"], capture_output=True, text=True)

