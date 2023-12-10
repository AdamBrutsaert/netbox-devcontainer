# NetBox Dev Container

This repository is made for developping plugins for NetBox via the usage of dev containers.  

The development container contains Python with Poetry and NodeJS installed.  
The root password is `netbox`.  
It also contains some basic VSCode extensions for convenience.

An instance of a development server of NetBox will be run so that it hot reloads whenever you make a modification.  
Plugins under the folder [plugins](/plugins/) will be automatically installed as editable inside the virtual env.

## Configure NetBox Version

You can set the version of NetBox inside the root [.env](/.env).  
Do not forget to run `docker compose build` whenever you change the version.

## Configure NetBox

You can edit the configuration of NetBox inside the [configuration](/configuration/) folder.  
Under this folder, you can also add modules to be installed inside the [requirements.txt](/configuration/requirements.txt) file.
