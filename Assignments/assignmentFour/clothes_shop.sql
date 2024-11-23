CREATE DATABASE clothes_shop;
USE clothes_shop;

CREATE TABLE stock_room (
item_id INT NOT NULL AUTO_INCREMENT,
item_type varchar(255),
number_in_stock INT,
PRIMARY KEY (item_id)
);

INSERT INTO stock_room
(item_type, number_in_stock)
VALUES
("Trousers", 60),
("Jacket", 30),
("Trainers", 24),
("T-shirt", 73);