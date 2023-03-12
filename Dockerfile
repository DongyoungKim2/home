# FROM genghisyang/pynecone-pip:latest

# RUN pip install pandas

FROM dongyoungkim/home:0.1.7

RUN rm -rf ./home 
RUN git clone https://github.com/DongyoungKim2/home.git ./home

WORKDIR /app/home

RUN pc init

WORKDIR /app/home

CMD ["pc", "run" ,"--env", "prod"]