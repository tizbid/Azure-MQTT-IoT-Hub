###  Azure IoT Telemetry Monitoring  

The Demo in this Repository, contains files for transferring data to Azure IoT Hub via MQTT protocol.
It extends further to show how to use this data to configure a Monitoring System using the following Azure services

* Azure Stream Analytics
* Power BI
* Azure blob storage


### Create Infastructure : `main.tf`

The terraform configuration file (main.tf) contains the infastructure codes. It creates the following resources:


* IoT Hub Service
* Azure Stream Analytics
* Azure blob storage

Use `terraform apply` to create the infastructure.

### Generate IoT data : `generate-data.py`
