# Scan Crawler

A project demonstrating the usage of Flask, Beautifulsoup crawler, AngularJS and Docker. 

### Local Development

#### 0. Prerequisites: 

	Install Python, Pip, virtualenv, virtualenvwrapper
	$ pip -V #Version of the file

#### 1. Clone the project:

	$ git clone <git-repo>
	$ cd <folder>

#### 2. Install packages:

	$ mkvirtualenv <anyname> # or workon <anyname> if you have already installed
	$ pip install -r requirements.txt

#### 3. Run the application:

	$ python manage.py runserver

#### 4. Configuration changes:
	$ # Change settings.py for port changes
	$ export DEBUG=false # Rerun the application for production server

### Docker 

#### 1. Build the image

	$ docker build -t scan-crawler .
	$ docker images # Verify the image in your local docker repo

#### 2. Run the image with your local port mapping	

	$ docker run -d -p 5000:5000 --name scan-crawler-service scan-crawler