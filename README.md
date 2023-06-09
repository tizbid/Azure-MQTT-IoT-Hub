###  Azure IoT Telemetry Monitoring  

The Project  contains files for transferring IoT data to Azure IoT Hub using MQTT protocol.
It extends further to show how to use this data to configure a Monitoring System using the following Azure services

* Azure Stream Analytics
* Power BI
* Azure blob storage


#### Create Infastructure : 

The terraform configuration file `main.tf` contains the infastructure codes. It creates the following resources:


* An IoT Hub Service
* An Azure Stream Analytics
* An Azure blob storage

Run `terraform apply` to create the infastructures.

#### Generate IoT data : 

`generate-data.py`, generates the IoT data, and transfers it to Azure IoT eventhub via MQTT using the Azure Python SDK


To view data uploads, from the Azure CLI, run the commandlet  `az iot hub monitor-events --hub-name <your-IoT-hubname> --device-id <your-device-id>`

#### Uploads
https://user-images.githubusercontent.com/56255193/231018415-3cb3a2d4-b4ef-470a-8863-2bb2fe27d4a0.mp4


#### Stream data

Stream analytics is manually configured. It accepts input data from IoT hub and outputs it to Grafana and a storage container.



![Demo-Architecture](img.jpg) 






