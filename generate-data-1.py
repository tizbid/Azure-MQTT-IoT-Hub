import time
import os
import ssl
import calendar
import datetime
import json
import random
from dotenv import load_dotenv
from paho.mqtt import client as mqtt


#load environment variables
load_dotenv()
    

device_id = os.environ.get('Device_ID')
iot_hub_name = os.environ.get('iot_hub_name')
sas_token = os.environ.get('Pri_Conn_String')

def connect_to_iothub():
    
   
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_log(client, userdata, level, buf):
        print("log: ",buf)

    def on_subscribe(client, userdata, mid, granted_qos):
        print('Subscribed for m' + str(mid))

    def on_message(client, userdata, message):
        print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
    
    

    client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311, clean_session=False)
    client.on_log = on_log
    client.tls_set_context(context=None)

    # Set up client credentials
    username = "{}.azure-devices.net/{}/api-version=2018-06-30".format(iot_hub_name, device_id)
    client.username_pw_set(username=username, password=sas_token)

    # Connect to the Azure IoT Hub
    client.on_connect = on_connect
    client.connect(iot_hub_name +".azure-devices.net", port=8883)
    client.on_message = on_message
    client.on_subscribe = on_subscribe 
    client.subscribe("device/{device_id}/messages/devicebound/#".format(device_id=device_id))

    return client



def publish_data(client):
    while True:
        # Generate random values for the wind turbine parameters
 
        tyme = time.strftime("%H:%M:%S", time.localtime())
        wind_speed = round(random.uniform(0, 50), 2)
        wind_direction = round(random.uniform(0, 360), 2)
        rotor_speed = round(random.uniform(0, 1000), 2)
        blade_angle = round(random.uniform(-5, 5), 2)
        power_output = round(random.uniform(0, 1000), 2)
        generator_rpm = round(random.uniform(0, 2000), 2)

        # Create a JSON message with the telemetry data
        telemetry = {
            "Time": tyme,	
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
            "rotor_speed": rotor_speed,
            "blade_angle": blade_angle,
            "power_output": power_output,
            "generator_rpm": generator_rpm
        }
        data_out1 = json.dumps(telemetry)
        client.publish("devices/{device_id}/messages/events/".format(device_id=device_id), payload=data_out1, qos=1, retain=False)
        print("Publishing Parameter data on devices/" + device_id + "/messages/events/",data_out1)
        time.sleep(5)
        


def main():
    client = connect_to_iothub()
    time.sleep(1)
    publish_data(client)
    client.loop_forever()


if __name__ == "__main__":
    main()