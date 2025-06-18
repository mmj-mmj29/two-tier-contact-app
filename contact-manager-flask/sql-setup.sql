CREATE DATABASE contactdb;
CREATE USER 'contactuser'@'localhost' IDENTIFIED BY 'contactpass';
GRANT ALL PRIVILEGES ON contactdb.* TO 'contactuser'@'localhost';
USE contactdb;

CREATE TABLE contacts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20)
);

EXIT;
