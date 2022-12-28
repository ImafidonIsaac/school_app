########### NOTE CODES ARE RUN FROM TOP TO BOTTOM ##################

###############Pull base image########################
#Import slim variant of python(Smaller size) and bullseye(latest release)
FROM python:3.11.1-slim-bullseye



###############Set 3 environment variables###############
#Disable automatic check for pip updates
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

#Python will not try to write .pyc files
ENV PYTHONDONTWRITEBYCODE 1

#Ensure our console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1



################## Set  work directory########################
#Use this path as the default location for all subsequent commands(Working Directory)
WORKDIR /code



#Install dependencies
#Copy the requirements.txt file from our local pc to the current working directory(The Image)
COPY ./requirements.txt .
#Running pip install (Run and install all its content)
RUN pip install -r requirements.txt


#Copy project
#Copy all files from current directory into the working directory on the image
COPY . .