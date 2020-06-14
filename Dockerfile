FROM python:3.8

MAINTAINER darrell.cox

COPY . /app
WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy

EXPOSE 8080

CMD ["python", "run.py"]
