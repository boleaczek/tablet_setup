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

Button names map to xsetwacom button names.

# Requirements
xsetwacom
xinput
digimend-kernel-drivers