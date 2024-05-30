#!/bin/bash

source /opt/netbox/venv/bin/activate

/opt/netbox/netbox/manage.py runserver "0.0.0.0:8000"
