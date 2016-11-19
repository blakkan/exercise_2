#! /bin/bash
psql -U postgres -c 'CREATE DATABASE "Tcount" owner postgres;'
psql -U postgres -d Tcount -c 'CREATE TABLE "Tweetwordcount" ( word VARCHAR UNIQUE primary key, count INT DEFAULT 0);'
