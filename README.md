# How to run
huion_setup.py <path to config>

# Configuration
```json
{
    "monitor" : "monitor_name",
    "buttons" : {
        "device_name" : {
            "Button 1" : "key 1",
            "Button 2" : "key 2"
        }
    }
}
```

monitor - ex.: DisplayPort-0, devices will be limited to that monitor only, monitor name can be found with xrandr

buttons:
* device_name - ex.: HUION Huion Tablet_HS611 Pad pad, can be wound with xinput or xsetwacom list devices
* Button X - maps to buttons from xsetwacom configuration options
* key - maps to keys from xsetwacom configuration option

# Requirements
* xsetwacom
* xinput
* digimend-kernel-drivers