# Simple AutoIndex 

A directory listing tool.

## Features

- Sortable
- Rememberable
- Efficient

## Requirements

- python 2.x
- uwsgi 2.x

## Installation on Ubuntu 12.04LTS

**Step 1:** Install the required packages

	sudo apt-get install python-dev python-pip git
	sudo pip install uwsgi
	git clone http://github.com/defool/autoindex.git
	cd autoindex
	pwd

**Step 2:**

Set **chdir** in autoindex/uwsgi.ini to the your full path name of **autoindex** directory

**Step 3:** Run uwsgi
	
	uwsgi uwsgi.ini # or nohup uwsgi uwsgi.ini &


## Configuration on Nginx

	server {
	    listen 800;
	    root /tmp/ # root directory for listing
	    try_files $uri @autoindex;    
	    location /autoindex { # static resources
	    	alias {path to autoindex directory}/assets;
	        expires 24h;
	    }
	    location @autoindex {
	    	uwsgi_pass 127.0.0.1:20001; # corresponding setting in uwsgi.ini
	    	include uwsgi_params;
	    }
	}

**root** and **alias** should be set manually.  

## Screenshot

![Screenshot](http://github.com/defool/autoindex/raw/master/screenshot.png)