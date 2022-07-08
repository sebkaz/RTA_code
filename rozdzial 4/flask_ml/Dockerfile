FROM python:3.8-slim

WORKDIR /app

COPY app.py .
COPY model.py .
COPY train.py . 
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN python3 train.py

ENTRYPOINT ["python3"]
CMD ["app.py"]