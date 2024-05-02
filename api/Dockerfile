FROM python:3.9

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
        htop \
        procps \
        tzdata \
        unzip \
        vim \
        zip \
        && \
        rm -rf /var/lib/apt/lists/*

# set time zone
ENV TZ America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /api
COPY api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY api/app app

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "app.app:app"]