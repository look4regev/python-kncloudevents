FROM python:3.7.3-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/* ./

CMD ["python", "httpDefault.py"]

