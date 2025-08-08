FROM python:3.10

WORKDIR /app

COPY cat-cular.py /app
COPY templates /app/templates

RUN pip install flask

EXPOSE 5000

CMD ["python", "cat-cular.py"]
