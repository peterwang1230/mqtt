import paho.mqtt.client as mqtt

def process_msg(client, userdata, message):
    print('message received', str(message.payload.decode('utf-8')))
    print('message topic=', message.topic)
    print('message qos=', message.qos)
    print('message retain flag=', message.retain)


client = mqtt.Client(client_id='subscriber-1')

client.on_message = process_msg

client.username_pw_set(username='roger', password='password')
client.connect('127.0.0.1', 1883, 60)

ret = client.subscribe('house/light')


client.loop_forever()