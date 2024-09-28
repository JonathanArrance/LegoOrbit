#!/bin/bash

#setup on the local machine for test and dev
#source your env variables first

docker network create --driver bridge --subnet 172.18.0.0/16 container_net

mkdir -p $(pwd)/db
mkdir -p $(pwd)/ssl
mkdir -p $(pwd)/json

touch $(pwd)/json/example.json

openssl req -newkey rsa:4096  -x509  -sha512  -days 365 -nodes -subj "/C=US/ST=NC/L=AnyTown/O=Home/CN=coinbasecollector.com" -out ./ssl/apicert_chain.crt -keyout ./ssl/api_private_key.key

sqlite3 ${DB_PATH}/lunar.db
sqlite3 ${DB_PATH}/lunar.db "CREATE TABLE if not exists LunarDates (ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, timestamp TEXT, jsonfile TEXT, phase TEXT)"

sqlite3 ${DB_PATH}/lunar.db "INSERT OR IGNORE INTO LunarDates (timestamp,jsonfile,phase) VALUES ('11111111111','example.json','crescent')"
