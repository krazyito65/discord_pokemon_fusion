FROM python:3.11
RUN apt-get update && apt-get install -y
WORKDIR /app/
COPY . /app/
RUN /bin/bash -c 'pip install -r requirements.txt'
RUN /bin/bash -c 'export UID'
CMD ["/bin/bash", "-c", "python3 poke_fuse.py"]