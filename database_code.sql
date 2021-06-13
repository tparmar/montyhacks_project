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
    person_id INTEGER,
    name TEXT NOT NULL,
    surgical_history TEXT NOT NULL,
    obstetric_history TEXT NOT NULL,
    medications TEXT NOT NULL,
    allergies TEXT NOT NULL,
    family_history TEXT NOT NULL,
    social_history TEXT NOT NULL,
    habits TEXT NOT NULL,
    immunization TEXT NOT NULL,
    developmental_history TEXT NOT NULL,
    demographics TEXT NOT NULL,
    medical_encounters TEXT NOT NULL,
    notes TEXT NOT NULL
);