FROM postgres:latest

RUN mkdir -p /docker-entrypoint-initdb.d
ADD create_db.sh /docker-entrypoint-initdb.d/

EXPOSE 5432
