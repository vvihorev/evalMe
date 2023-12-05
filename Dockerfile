FROM python:3-slim
ADD . /
RUN pip install bottle
EXPOSE 8069
CMD [ "python", "./main.py" ]
