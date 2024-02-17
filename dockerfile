FROM ubuntu:20.04
RUN mkdir /app
WORKDIR /app

RUN apt-get update

RUN apt-get install --fix-missing -y \
    curl \
    python3 \
    python3-pip \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*  && \
    apt-get purge --auto-remove && \
    apt-get clean


COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade flask-cors

COPY . /app

RUN chmod -R +x /app/

ENTRYPOINT ["python3", "api/app.py"]
