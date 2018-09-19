# Use an official Python runtime as a parent image
FROM frolvlad/alpine-python-machinelearning

COPY ./ /app

RUN pip install -r /app/requirements.txt

CMD python3 /app/src/app.py
