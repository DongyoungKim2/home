FROM holocloud/pynecone:latest

RUN apt-get install git -y
 
RUN mkdir /opt/app

RUN git clone https://github.com/DongyoungKim2/home.git /opt/app

RUN cd /opt/app/home

# CMD ["pc run"]