FROM genghisyang/pynecone-pip:latest

RUN pip install pandas

RUN git clone https://github.com/DongyoungKim2/home.git ./home

WORKDIR /app/home

RUN pc init

WORKDIR /app/home

CMD ["pc", "run" ,"--env", "prod"]