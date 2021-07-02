import paho.mqtt.client as mqtt


def connect_msg():
    print('Connect to Broker')


def publish_msg():
    print('Message Published')


client = mqtt.Client(client_id='publish-1')

client.on_connect = connect_msg()
client.on_publish = publish_msg()


#client.connect('127.0.0.1', 1883)
client.username_pw_set(username='pub_client', password='password')
client.connect('127.0.0.1', 1883, 60)
# client.connect('192.168.50.172', 1883)

ret = client.publish('house/light', 'on')


client.loop()
