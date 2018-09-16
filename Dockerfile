# Use an official Python runtime as a parent image
FROM frolvlad/alpine-python-machinelearning

CMD python3 -c 'import numpy; print(numpy.arange(3))'