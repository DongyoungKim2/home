# FROM genghisyang/pynecone-pip:latest

# RUN pip install pandas

FROM dongyoungkim/home:0.1.7

RUN pip install --upgrade pynecone

WORKDIR /app

RUN rm -rf /app/home

WORKDIR /app

RUN git clone https://github.com/DongyoungKim2/home.git 

WORKDIR /app/home

RUN pc init

WORKDIR /app/home

CMD ["pc", "run" ,"--env", "prod"]