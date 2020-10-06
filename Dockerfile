FROM python:3.8.5

RUN mkdir /ExercicioUbiwhere

WORKDIR /ExercicioUbiwhere

RUN pip install -Iv Django==3.1.2

RUN pip install -Iv djangorestframework==3.12.1

RUN pip install -Iv psycopg2==2.8.6

COPY . .