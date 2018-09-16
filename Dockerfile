# Use an official Python runtime as a parent image
FROM frolvlad/alpine-python-machinelearning

COPY . /app

CMD python3 /app/src/local_runner.py
