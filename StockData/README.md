Step 1: 
Start the zookeper and kafka services.

Step 2:
Get the api key by visiting the site https://www.alphavantage.co/support/#api-key

Step 3:
Go through the documentation of stock api and get the python code for Time Series Stock APIs.

Step 4: 
Write the python code on a producer.py file and add the api key using the .env file

Step 5: 
Write the python code on a consumer.py file to display stock data and create a text file and store the output into it.

Step 6: 
Now start all servers of hdfs by the start-all.sh command and create a directory on hdfs as Kafka_Stock_Data using subprocess

Step 7: 
Now copy the output file of consumer.py to hdfs by using copyFromLocal command in sub process

$ hdfs dfs -mkdir -p /Kafka_Stock_Data

$ hdfs dfs -copyFromLocal /home/namratha/Documents/Kafka/StockData/StockData.txt /Kafka_Stock_Data/StockData.txt




