FROM python:3.9.2-alpine

WORKDIR /app
EXPOSE 5000

RUN adduser -D app
USER app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
