# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}



# Define the provider (in this case, Azure)
provider "azurerm" {
  features {}
  skip_provider_registration = true
}

# Define the resource group
resource "azurerm_resource_group" "RG" {
  name     = "IoT-Monitoring-RG"
  location = "westeurope"
}

# Define the IoT Hub
resource "azurerm_iothub" "iothub" {
  name                = "VT-iothub100"
  resource_group_name = azurerm_resource_group.RG.name
  location            = azurerm_resource_group.RG.location

  sku {
    name     = "B1"
    capacity = 1
  }
}

# Define the Stream Analytics job
resource "azurerm_stream_analytics_job" "stream_analytics_job" {
  name                = "VT-iothub100-stream-job"
  resource_group_name = azurerm_resource_group.RG.name
  location            = azurerm_resource_group.RG.location
  streaming_units     = 1

  transformation_query = <<QUERY
    SELECT
        *
    INTO
        [IoT-Monitoring-RG].output
    FROM
        [IoT-Monitoring-RG].input TIMESTAMP BY timeCreated
QUERY
}



# Define the storage account for the Function App
resource "azurerm_storage_account" "storage_account" {
  name                     = "allstorage100"
  resource_group_name      = azurerm_resource_group.RG.name
  location                 = azurerm_resource_group.RG.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
