-- Script that creates database and cities table
-- Creates database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses the created database
USE hbtn_0d_usa;
-- Creates cities table with foreign key reference to states
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
