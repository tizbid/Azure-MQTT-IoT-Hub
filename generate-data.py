import json
import random
import asyncio
import os
import time
from dotenv import load_dotenv
from azure.iot.device.aio import IoTHubDeviceClient

#load environment variables
load_dotenv()


async def send_data(msg_no):
    
    conn_str = os.getenv("Pry_Conn_String")
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    await device_client.connect()
    
    
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
        
        data = json.dumps(telemetry)
        
        msg = "for device:/" + os.getenv("Device_ID")+ "/messages/events/",data
        
        # Send the message.
        print("Sending message # + str(i) + : {}".format(msg) )
        await device_client.send_message(data)
        print ( "Message successfully sent" )
        time.sleep(1)
        
        

        # Shut down the client
        #device_client.shutdown()
            
        
if __name__ == "__main__":
    msg_no = 100
    asyncio.run(send_data(msg_no))