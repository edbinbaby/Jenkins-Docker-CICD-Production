FROM python:3.12

WORKDIR /app

COPY backend .

RUN pip install flask

CMD ["python","app.py"]
