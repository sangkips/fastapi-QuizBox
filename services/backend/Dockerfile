FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt update && apt install -y g++ libpq-dev gcc musl-dev

COPY requirements.txt .

#RUN python3 -m pip install -r requirements.txt --no-cache-dir
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
