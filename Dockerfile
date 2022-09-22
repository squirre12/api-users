FROM python:3.9
WORKDIR /code
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]


