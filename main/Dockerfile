FROM python:3.12.0
ENV PYTHONUNBUFFERED 1
WORKDIR /flask
COPY requirements.txt /flask/requirements.txt
RUN pip install -r requirements.txt
COPY . /flask/

CMD python3 main.py