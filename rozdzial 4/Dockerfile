FROM python:3.8-slim

WORKDIR /app

COPY app1.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app1.py"]