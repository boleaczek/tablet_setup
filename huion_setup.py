import json
import os

def filter_devices(xinput_output):
    xinput_output = xinput_output.split("\n")
    xinput_huion_devices = [device for device in xinput_output if "Huion" in device]

    huion_devices = []
    for xinput_huion_device in xinput_huion_devices:
        dev_name_start = xinput_huion_device.find("HUION")
        dev_name_end = xinput_huion_device.find("\t")
        huion_device_name = xinput_huion_device[dev_name_start: dev_name_end]
        huion_devices.append(huion_device_name)

    return huion_devices

with open("config.json") as cfg_file:
    cfg = json.load(cfg_file)
    huion_devices = filter_devices(os.popen("xinput").read())