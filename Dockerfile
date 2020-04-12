FROM python:3.6
ADD . /application
WORKDIR /application
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]