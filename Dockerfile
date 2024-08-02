FROM ubuntu:22.04

RUN apt update -y && apt upgrade -y && apt install fortune-mod netcat sudo cowsay -y 

WORKDIR /cowsay-app
COPY . .

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

USER docker

EXPOSE  4499
ENTRYPOINT ["sh","-c","export PATH=$PATH:/usr/games && ./wisecow.sh"]

