FROM python:3.12

WORKDIR /app

COPY backend/ .

RUN pip install flask flask-cors

EXPOSE 5000

CMD ["python","app.py"]
