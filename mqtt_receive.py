import paho.mqtt.client as mqtt
import time
import os

LOGFILE = "log.txt"

if not os.path.exists(LOGFILE):
    f = open(LOGFILE, "w")
    f.close()


def on_connect(mqttc, obj, flags, rc):
    print("Connected successfully!")


def on_message(mqttc, obj, msg):
    print("From " + msg.topic + " received:")
    print(msg.payload.decode("utf-8") + "\n")
    with open(LOGFILE, "a") as f:
        out = f"{msg.topic} {time.asctime(time.localtime(time.time()))}: {msg.payload.decode('utf-8')}\n"
        f.write(out)
        f.close()

    if msg.payload.decode("utf-8") == "END":
        print("Closing down!")
        raise SystemExit


mqttc = mqtt.Client("log-client")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("127.0.0.1")
mqttc.subscribe("test/#", 0)

mqttc.loop_forever()
