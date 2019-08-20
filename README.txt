Build image 

$ docker build .

Run docker image

$ docker run --name webserverapi -d -p 8080:8080

In a python command shell outside of the docker container, run:

$ python app/test/test.py