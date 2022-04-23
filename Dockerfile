FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin


WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install --upgrade pip
# solve cffi problem
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers \
    && apk add libffi-dev
RUN pip install -r requirements.txt

CMD sleep 10 && \
    python manage.py makemigrations --noinput && \
    python manage.py migrate --noinput && \
#    python manage.py collectstatic --noinput &&\
    python manage.py createsuperuser --user admin --email admin@example.com --noinput ; \
    gunicorn -b 0.0.0.0:8000 store.wsgi:application
