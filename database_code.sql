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