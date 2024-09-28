#!/bin/bash

mkdir -p ${DB_PATH}
mkdir -p $(pwd)/ssl
mkdir -p $(pwd)/json

openssl req -newkey rsa:4096  -x509  -sha512  -days 365 -nodes -subj "/C=US/ST=NC/L=AnyTown/O=Home/CN=legoorbit" -out /etc/api/ssl/apicert_chain.crt -keyout /etc/api/ssl/api_private_key.key

sqlite3 ${DB_PATH}/lunar.db
sqlite3 ${DB_PATH}/lunar.db "CREATE TABLE if not exists LunarDates (ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, timestamp TEXT, jsonfile TEXT, phase TEXT)"

sqlite3 ${DB_PATH}/lunar.db "INSERT OR IGNORE INTO LunarDates (timestamp,jsonfile,phase) VALUES ('11111111111','example.json','crescent')"

python3 /opt/orbit/orbit.py &

gunicorn -b 0.0.0.0:9030 --reload --access-logfile api_access.log --error-logfile api_error.log --log-level debug --timeout 120 -w 2 orbit_api &
/bin/sh -c envsubst < /nginx-default.conf > /etc/nginx/nginx.conf && exec nginx -g 'daemon off;' &