# Python base image. Get this from dockerhub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
# Set your working directory
WORKDIR /usr/src/app

# Install dependencies required by the image
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.1 && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

# Copy and mount the project to the working directory
COPY . ./

CMD poetry run alembic upgrade head && \
    poetry run uvicorn --host=0.0.0.0 app.main:app

