## Setup Instructions
1- terminal: git clone https://github.com/Alexa-Fahel/docker_assignment.git
2- termainal: cd docker_assignment
3- open the docker app in the background
4- terminal: docker-compose up -d --build

to check the results go to the volumes tab in the docker app, go to docker_assignment_logs, and check logs.txt

## Assignment Summarized
1- producer.py generates random data every 2 seconds and sends it to the data consumer
2- consumer.py listens for incoming data on port 5000 and writes it to logs.txt
3- The consumer dockerfile copies the python script and defines a volume to store the logs inside
4- The producer dockerfile to copies the python script and exposes port 5000
5- docker-compose.yml creates a docker network between the the producer and consumer containers  
