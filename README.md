# pspProject

This is the completely deployable `Django` backend for `https://github.com/Ommanimesh2/NASA_SPACE_APPS.git` : Solar Probe Reimagined

## Solar Probe Reimagined

An interactive web application to take you aboard the Parker Solar Probe. What is Parker Solar Probe? 
A scientific mission to unlock the mysteries of the Sun's corona and solar wind. It studies the corona and 
solar winds as it goes around a revolution of 88 days and comes as close to Sun as any spacecraft has ever been.

## Installation

Download and then install python from [Python 3.10.7](https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe) or from `https://www.python.org/downloads/`
Clone the git repository `git clone https://github.com/NanoNish/pspProject.git`.

### Virtual Environment

Create a virtual environment `python -m venv pspenv`
Run the virtual environment `.\pspenv\Scripts\activate`

To deactivate just run `deactivate`

### Installing packages

Install the packages in venv
`pip install -r requirements.txt`

## Run the server

First create a superuser
`python manage.py createsuperuser`

Now run the server
`python manage.py runserver`

The server will be running at `http://127.0.0.1:8000/`

## API endpoints

The PSP Dataset can be accessed using 
`http://127.0.0.1:8000/mergedata/data/{number}`

The ImageData can be accessed using
`http://127.0.0.1:8000/imagedata/image/{number}`

To see all the possible methods go to
`http://127.0.0.1:8000/mergedata/data` for PSP Dataset
`http://127.0.0.1:8000/imagedata/image` for ImageData
