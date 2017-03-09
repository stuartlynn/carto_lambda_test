FROM amazonlinux:2016.09

RUN curl https://bootstrap.pypa.io/get-pip.py |  python 
RUN pip install virtualenv 

