# Another Meross LAN

Python library for controlling *Meross* devices over LAN with direct HTTP connection bypassing Meross cloud. It is a heavily modified, simple, super light fork of the [meross_lan](https://github.com/krahabb/meross_lan) Home Assistant Integration by [krahabb](https://github.com/krahabb).

## Installation
Just download the repository.

### Usage
You need to change const.py file:
```python
# Meross device LAN IP
DEVICE_IP = "192.168.XXX.XXX"
# Meross device key, 32 character alphanumeric string,
# e.g 2a1278l78784dbiv8i1y1weuhrikz9mh
DEVICE_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
with your device's LAN IP and KEY. Search Google how to obtain device key... There are few diffrent, not very simple, long to explain ways so just do some research... I personaly had to temporally setup VirtualBox "Home Assistant", install [meross_lan](https://github.com/krahabb/meross_lan) add-on and get the device key while setting up my Meross device with meross_lan which gets it from Meross cloud and  and shows it. So your device must be in your Meross cloud already.
After all this is done, you are goot to go... See example_main.py for simple code example how to control your Meross device.
For specific namespace and payload code for your particular device dig into [meross_lan](https://github.com/krahabb/meross_lan) and  [MerossIot](https://github.com/albertogeniola/MerossIot) code. Also see [Meross Device/Appliance Protocol](https://github.com/arandall/meross/blob/main/doc/protocol.md) and [How a device is configured](https://github.com/arandall/meross/blob/main/doc/provisioning.md) to get better understanding how all works.

## Special credits and Thanks to:
- [@krahabb](https://github.com/krahabb)
- [@albertogeniola](https://github.com/albertogeniola)
- [@arandall](https://github.com/arandall)
for their great work!!!