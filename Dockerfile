FROM python:3.6
MAINTAINER Muhammad Omar <Muhammad.omar.eg@gmail.com>
EXPOSE 80
COPY ./app /app
WORKDIR /app/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
