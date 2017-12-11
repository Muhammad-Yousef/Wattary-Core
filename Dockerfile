FROM python:3.6
MAINTAINER Muhammad Omar
EXPOSE 80
COPY ./app /app
WORKDIR /app/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
