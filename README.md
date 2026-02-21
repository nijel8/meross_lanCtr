# Another Meross LAN

Python library for controlling *Meross* devices over LAN with direct HTTP connection bypassing Meross cloud. It is a heavily modified, simple, super light fork of the [meross_lan](https://github.com/krahabb/meross_lan) Home Assistant Integration by [krahabb](https://github.com/krahabb).

## Installation
Download the [repository](https://github.com/nijel8/meross_lanCtr/archive/refs/heads/master.zip) and run [get_device_key.py](https://github.com/nijel8/meross_lanCtr/blob/master/meross_lan/get_device_key.py) in meross_lan folder.
Enter your Meross account email and password to get the key for controlling  Meross devices over LAN.
Change [const.py](https://github.com/nijel8/meross_lanCtr/blob/master/meross_lan/const.py) file with your device IP and key:
```python
# Meross device LAN IP
DEVICE_IP = "192.168.XXX.XXX"
# Meross device key, 32 character alphanumeric string,
# e.g 2a1278l78784dbiv8i1y1weuhrikz9mh
DEVICE_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Usage
See [example_main.py](https://github.com/nijel8/meross_lanCtr/blob/master/example_main.py) for simple code example how to control your Meross device.
For specific namespace and payload code for your particular device dig into [meross_lan](https://github.com/krahabb/meross_lan) and  [MerossIot](https://github.com/albertogeniola/MerossIot) code. Also see [Meross Device/Appliance Protocol](https://github.com/arandall/meross/blob/main/doc/protocol.md) and [How a device is configured](https://github.com/arandall/meross/blob/main/doc/provisioning.md) to get better understanding how all works.

## Special credits and Thanks to:
- [@krahabb](https://github.com/krahabb)
- [@albertogeniola](https://github.com/albertogeniola)
- [@arandall](https://github.com/arandall)

for their great work!!!
