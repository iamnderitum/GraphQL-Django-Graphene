FROM python:3.9
ENV PYTHONUNBUFFERED = 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
COPY . /app/
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /app/ 
RUN chmod +x /app/docker-entrypoint.sh
#CMD /app/docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
