import subprocess
'''
response = subprocess.run("echo 'Join the Dark Side!' 1>&2",
                          shell=True,
                          stderr=subprocess.PIPE)
print(response.stderr)
print(response.stdout)
print(response.args)
print(response.returncode)
print(response.check_returncode())
'''

# //joshu//OneDrive//Desktop//Vim3Utils
# cat /sys/class/mcu/usb_pcie_switch_mode
# echo 0 > /sys/class/mcu/usb_pcie_switch_mode
# echo 1 > /sys/class/mcu/usb_pcie_switch_mode
# echo 1 > /sys/class/mcu/poweroff

response = subprocess.run('ls',
                          shell=True,
                          stderr=subprocess.PIPE)
print(response.stderr)
print(response.stdout)
print(response.returncode)

response = subprocess.run('cat /sys/class/mcu/usb_pcie_switch_mode',
                          shell=True,
                          stderr=subprocess.PIPE)
print(response.stderr)
print(response.stdout)
print(response.returncode)


import os
import sys
import subprocess

if os.geteuid() == 0:
    print("We're root!")
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()