FROM python:3.9.2-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]

EXPOSE 5000