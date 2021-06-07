-- SQLite
CREATE TABLE people(
    id INTEGER,
    name TEXT NOT NULL,
    birth NUMERIC,
    PRIMARY KEY(id)
);
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
    type TEXT NOT NULL
);