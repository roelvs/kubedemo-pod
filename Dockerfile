FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN ls -lah

EXPOSE 5000

CMD ["python", "./demopage.py"]
