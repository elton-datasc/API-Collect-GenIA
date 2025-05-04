    FROM python:3.10-alpine

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y gcc && \ 
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
