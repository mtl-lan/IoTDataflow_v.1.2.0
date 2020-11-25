# IoT Project: E-Coating Streaming Data Pipeline simulator

## Data source 
Data we used in this project is E-coating ultrafiltration maintenance dataset from [kaggle](https://www.kaggle.com/boyangs444/process-data-for-predictive-maintenance). 
It is a real dataset from an electrophoresis painting plant where has been recently deployed an IIoT system.

## Project main scope 
This IoT project contains a local python APP to read source csv file in line by sleep 1 second and then write each row into a seperate csv file with timestamp added on the file name. 
It also contains a docker-compose file that will start up 5 services that will demonstrate the use case of using Kafka-Connect source connectors to pull files from an FTP server, post it to a Kafka topic which will be read by a consumer application. For this demo, we will be using Confluent Kafka.
In addition, a mysql container with UI is also included in the docker-compose file which can be further used by another local app to read data from kafka and push data into mysql database. 

1. Zookeeper
2. Kafka
3. Kafka-Connect
4. FTP Server
5. Consumer Application

## Data ingestion Flow Chart 

![picture](/home/rebecca/IdeaProjects/IoTDataflow_v.1.2.0/dataflow.PNG)

## Prequisites
- The only prequisite to run is to have docker installed for respective OS. 
Click [here](https://www.docker.com/products/docker-desktop) to go to the docker webpage.

# How to Run
## Values to Edit
* Under *services -> ftp-server -> volumes* in the docker compose, you would need to replace with your local file system path
* Under your local FTP folder, create an **archived** and **error** folder.
* Currently the *Consumer* service is porting to port *8080* on the host machine, if that port is not available, you would need to change in the *docker-compose* to one that is.


## Commands
Open up terminal or command prompt and run:

     docker-compose build
     docker-compose up


# How to Test
After *docker-compose* has been ran, go to the following link:
    
    localhost:8080/kafka/getmessages

From here you will see the page is in a constant stage of loading. This is the *consumer* working and it will consume streams sent by Kafka-Connect to *kafka-sftp-demo* topic.

# Notable Links
* [Kafka Quick Start Guide](https://kafka.apache.org/quickstart)
* [Kafka-Connect-SFTP Plugin Download](https://www.confluent.io/hub/confluentinc/kafka-connect-sftp)
* [SFTP Source Connector for Confluent Platform](https://docs.confluent.io/current/connect/kafka-connect-sftp/source-connector/index.html)
* [atmoz SFTP docker hub](https://hub.docker.com/r/atmoz/sftp/)


