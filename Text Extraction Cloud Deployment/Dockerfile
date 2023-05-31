FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip sudo

RUN useradd -m pratham

RUN chown -R pratham:pratham /home/pratham/

COPY --chown=pratham . /home/pratham/app/

USER pratham

RUN pip3 install --upgrade pip

RUN cd /home/pratham/app/ && python3 -m pip cache purge

RUN cd /home/pratham/app/ && pip3 install -r requirements.txt

WORKDIR /home/pratham/app

EXPOSE 8080

ENTRYPOINT python3 api.py