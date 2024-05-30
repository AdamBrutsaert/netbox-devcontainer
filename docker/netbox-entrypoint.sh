#!/bin/bash

set -e
source /opt/netbox/venv/bin/activate

if [ -f "/opt/netbox/netbox/netbox/configuration/requirements.txt" ]; then
  pip install -r /opt/netbox/netbox/netbox/configuration/requirements.txt
fi

if [ -d "/opt/plugins" ]; then
  # Find directories with pyproject.toml files
  find /opt/plugins -type f -name "pyproject.toml" -print0 | while IFS= read -r -d '' plugin; do
    pip install -e $(dirname "$plugin")
  done
fi

if ! /opt/netbox/netbox/manage.py migrate --check >/dev/null 2>&1; then
  /opt/netbox/netbox/manage.py migrate --no-input
  /opt/netbox/netbox/manage.py trace_paths --no-input
  /opt/netbox/netbox/manage.py remove_stale_contenttypes --no-input
  /opt/netbox/netbox/manage.py reindex --lazy
  /opt/netbox/netbox/manage.py clearsessions
fi

exec "$@"
