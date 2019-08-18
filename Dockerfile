FROM alpine:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python /app/app.py
