FROM python:3

WORKDIR /usr/src/app

COPY src ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
