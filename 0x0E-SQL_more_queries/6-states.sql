-- Script that creates database and states table
-- Creates database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses the created database
USE hbtn_0d_usa;
-- Creates states table with auto-increment primary key
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
