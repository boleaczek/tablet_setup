import json
import os

with open("config.json") as cfg_file:
    cfg = json.load(cfg_file)
    huion_devices = os.popen("xinput").read()