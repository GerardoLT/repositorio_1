FROM python:3.10.11-slim

WORKDIR /p1
COPY servicios ./servicios
COPY logica ./logica

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install -r ./servicios/requirements.txt
# ENV PYTHONPATH=/paid
ENV PYTHONPATH="$PYTHONPATH:/p1"

EXPOSE 8000
CMD ["python", "./servicios/manage.py", "runserver", "0.0.0.0:8000"]