FROM python:3.11-bullseye

ARG VERSION=master

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/netbox/.local/bin:${PATH}"
ENV VERSION=${VERSION}

RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
  && apt install -y nodejs

RUN git clone -b "${VERSION}" --depth 1 https://github.com/netbox-community/netbox.git /opt/netbox

RUN groupadd --gid 1000 netbox \
  && useradd --uid 1000 --gid 1000 -m "netbox" \
  && echo "netbox:netbox" | chpasswd \
  && chown -R "netbox:netbox" /opt/netbox

USER netbox

RUN python3 -m pip install --user --upgrade pip setuptools \
  && python3 -m pip install --user poetry \
  && poetry config virtualenvs.in-project true

WORKDIR /app

CMD [ "tail", "-f", "/dev/null" ]
