FROM genghisyang/pynecone-pip:latest

RUN mkdir /opt/app

RUN cd /opt/app

RUN git clone https://github.com/DongyoungKim2/home.git 

RUN cd /opt/app/home

RUN pip install pandas

RUN pc init

CMD ["pc run --env prod"]