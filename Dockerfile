FROM python:3.7
COPY . /app
WORKDIR /app
ENV STORE_IN_MEM=False
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
