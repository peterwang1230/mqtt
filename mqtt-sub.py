import paho.mqtt.client as mqtt
import json

def process_msg(client, userdata, message):
    print('message received', str(message.payload.decode('utf-8')))
    m_decode = str(message.payload.decode("utf-8","ignore"))
    train_cmd = json.loads(m_decode) # Converting from Json to dict Object
    print(train_cmd)
    print('message topic=', message.topic)
    print('message qos=', message.qos)
    print('message retain flag=', message.retain)


client = mqtt.Client(client_id='subscriber-1')

client.on_message = process_msg

client.username_pw_set(username='roger', password='password')
client.connect('127.0.0.1', 1883, 60)

ret = client.subscribe('train/v1/go')


client.loop_forever()