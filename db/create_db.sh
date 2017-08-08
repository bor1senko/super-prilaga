#!/bin/sh

set -e
POSTGRES="psql"

export PGUSER="$POSTGRES_USER"

$POSTGRES -E <<EOSQL
CREATE DATABASE spiner_db;
CREATE USER admin WITH password 'qwerty12345';
GRANT ALL ON DATABASE spiner_db TO admin;
EOSQL
