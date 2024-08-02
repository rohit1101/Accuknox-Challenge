FROM ubuntu:22.04

RUN apt update -y && apt upgrade -y && apt install fortune-mod netcat cowsay -y 

WORKDIR /cowsay-app
COPY . .
RUN chmod +x ./wisecow.sh

EXPOSE  4499
ENTRYPOINT ["sh","-c","export PATH=$PATH:/usr/games && ./wisecow.sh"]

