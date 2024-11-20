-- Script that creates table id_not_null
-- Creates table with default id value and name field
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
