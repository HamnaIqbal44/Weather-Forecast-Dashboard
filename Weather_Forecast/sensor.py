# import paho.mqtt.client as mqtt
# import pandas as pd
# from datetime import datetime
#
#
# def on_connect(client, userdata, flags, rc):
#     print(f"Connected with result code {rc}")
#     # subscribe, which need to put into on_connect if reconnect after losing the connection with the broker,
#     # it will continue to subscribe to the raspberry/topic
#     client.subscribe("A2_Temperature")
#     print("subscribed A2_Temperature")
#     client.subscribe("STC_Temperature")
#     print("subscribed STC_Temperature")
#     client.subscribe("B_Hostel_Temperature")
#     print("subscribed B_Hostel_Temperature")
#     client.subscribe("SPCAI_Temperature")
#     print("subscribed SPCAI_Temperature")
#
#
# # the callback function, it will be triggered when receiving messages
# df = pd.DataFrame(columns=["Time", "A2_Temperature", "STC_Temperature", "B_Hostel_Temperature", "SPCAI_Temperature"])
#
#
# def on_message(client, userdata, msg):
#     print(f"{msg.topic} {msg.payload}")
#     print(msg.payload)
#     rec_msg = msg.payload.decode("utf-8")
#     topic = msg.topic
#     print(msg.topic)
#     print(rec_msg)
#     print(type(msg.topic))
#     print(type(rec_msg))
#     if topic == "A2_Temperature":
#         time = datetime.now()
#         seconds = time.strftime('%M:%S')
#         df1 = pd.DataFrame({'Time': seconds, "A2_Temperature": [rec_msg, ]})
#         d1 = pd.concat([df, df1])
#         d1.to_csv('sensor_data.csv', mode='a',index=False)
#         print("send data a2 enter")
#     elif topic == "STC_Temperature":
#         time = datetime.now()
#         seconds = time.strftime('%M:%S')
#         df2 = pd.DataFrame({'Time': [seconds, ], "STC_Temperature": [rec_msg, ]})
#         d2 = pd.concat([df, df2])
#         print(d2)
#         d2.to_csv('sensor_data.csv', mode='a',index=False)
#         print("send data stc enter")
#     elif topic == "B_Hostel_Temperature":
#         time = datetime.now()
#         seconds = time.strftime('%M:%S')
#         df3 = pd.DataFrame({'Time': [seconds, ], "B_Hostel_Temperature": [rec_msg,]})
#         d3 = pd.concat([df, df3])
#         print(d3)
#         d3.to_csv('sensor_data.csv', mode='a',index=False)
#         print("send data bhostel enter")
#     else:
#         time = datetime.now()
#         seconds = time.strftime('%M:%S')
#         df4 = pd.DataFrame({'Time': [seconds, ], "SPCAI_Temperature": [rec_msg,]})
#         d4 = pd.concat([df, df4])
#         print(d4)
#         d4.to_csv('sensor_data.csv', mode='a', index=False)
#         print("senddataspcai enter")
#
#
# data = []
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
#
#
# # set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send
# # the will message to other clients
# client.will_set('ras', b'{"status": "Off"}')
#
# # create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
# client.connect("10.1.36.216", 1883, 60)
#
# # set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
# client.loop_forever()
#
