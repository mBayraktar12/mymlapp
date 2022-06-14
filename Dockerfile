FROM python:3

WORKDIR /usr/local/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r  requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app/main.py","--host=0.0.0.0"]