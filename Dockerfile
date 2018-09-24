# Use an official Python runtime as a parent image
FROM python:3

COPY ./ /app

RUN pip install -r /app/requirements.txt
WORKDIR "/app/src/"

# CMD python3 -m http.server
CMD gunicorn --reload -b '0.0.0.0:8000' app
