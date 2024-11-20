-- Script that creates table force_name
-- Creates table with id and non-null name field
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
