-- Script that creates table unique_id
-- Creates table with unique id and name field
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
