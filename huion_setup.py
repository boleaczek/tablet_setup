import json
import os

def limit_monitors(monitor, huion_devices):
    for huion_device, device_id in huion_devices.items():
        os.system('xinput map-to-output {} {}'.format(device_id, monitor))

def configure_buttons(buttons_cfgs):
    for (device_name, button_cfg) in buttons_cfgs.items():
        for (button, key) in button_cfg.items():
            os.system("xsetwacom --set \"{}\" {} \"{}\"".format(device_name, button, key))

def filter_devices(xinput_output):
    xinput_output = xinput_output.split("\n")
    xinput_huion_devices = [device for device in xinput_output if "Huion" in device]

    huion_devices = {}
    for xinput_huion_device in xinput_huion_devices:
        dev_id_start = xinput_huion_device.find("=") + 1
        dev_id_end = dev_id_start + 2
        dev_id = xinput_huion_device[dev_id_start: dev_id_end]

        dev_name_start = xinput_huion_device.find("HUION")
        dev_name_end = xinput_huion_device.find("id")
        dev_name = xinput_huion_device[dev_name_start: dev_name_end].strip()

        huion_devices[dev_name] = dev_id

    return huion_devices

with open("config.json") as cfg_file:
    cfg = json.load(cfg_file)
    huion_devices = filter_devices(os.popen("xinput").read())
    limit_monitors(cfg["monitor"], huion_devices)