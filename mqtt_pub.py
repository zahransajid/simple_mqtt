import paho.mqtt.publish as publish


print("Type anything to send it to the log topic. Type q to quit.")
print("Typing END will stop the receiver.")

while True:
    msg = input(">>> ")
    if msg.lower() == "q":
        break
    publish.single("test/log", msg, hostname="127.0.0.1")
