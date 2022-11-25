#Install image of python. For APP(P.S: prefer use "python:3.8.12-slim")
FROM python:3.9.0
#Maintainer of docker
MAINTAINER Dmitriy Voronkov 'voronkov.vot@yandex.ru'
#Workdirectory for next instraction in container-Files of programm will be here
WORKDIR /opt/programm
#copy from this directory in container
COPY . /opt/programm
#Installing tkinter(version 8.6) inside a container
RUN apt-get install tk8.6 -y
#RUN any commands
CMD ["python3", "main.py"]
