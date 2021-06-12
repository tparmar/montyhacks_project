-- SQLite
CREATE TABLE hospital(
    id INTEGER,
    name TEXT NOT NULL,
    opening TEXT NOT NULL,
    closing TEXT NOT NULL
);
CREATE TABLE users(
    id INTEGER,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    type TEXT NOT NULL,
    birth NUMERIC,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE records(
    



);