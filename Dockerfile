FROM python:3.11-bullseye

ARG VERSION=master

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VERSION=${VERSION}

RUN apt update \
  && apt install -y \
    git \
    curl \
    postgresql \
    redis-server \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libpq-dev \
    libssl-dev \
    zlib1g-dev

RUN mkdir -p /opt/netbox \
  && cd /opt/netbox \
  && git clone -b "${VERSION}" --depth 1 https://github.com/netbox-community/netbox.git .

RUN groupadd --gid 1000 netbox \
  && useradd --uid 1000 --gid 1000 -m "netbox" \
  && chown -R "netbox:netbox" /opt/netbox

USER netbox

RUN python3 -m venv /opt/netbox/venv \
  && . /opt/netbox/venv/bin/activate \
  && pip install --upgrade pip \
  && pip install wheel \
  && pip install -r /opt/netbox/requirements.txt

WORKDIR /opt/netbox/

COPY docker/docker-entrypoint.sh .
COPY docker/launch-netbox.sh .
COPY docker/housekeeping.sh .

ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD [ "./launch-netbox.sh" ]
