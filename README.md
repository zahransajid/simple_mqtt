# Code for a simple receive-publish app over MQTT

`mqtt_receive.py` once started will log incoming messages over the `test\#` topics to stdout and `log.txt`.

`mqtt_pub` gives a simple interface to send messages.

Requires mosquitto to be installed, run `start_server.bat` to start the MQTT server.
