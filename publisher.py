import paho.mqtt.publish as publish
publish.single("ifn649", "Hello World", hostname="3.106.232.128")
print("Done")
