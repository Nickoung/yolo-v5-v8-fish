import os
import subprocess

folder_path = r'C:\Users\zhy02\Desktop\urp\ui'
for filename in os.listdir(folder_path):
    if filename.endswith('.ui'):
        ui_file = os.path.join(folder_path, filename)
        py_file = os.path.join(folder_path, filename[:-3] + '.py')
        command = f'pyuic5 -x {ui_file} -o {py_file}'
        subprocess.run(command)