-- Script that creates database and user with SELECT privilege
-- Creates database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privilege to user on specified database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
