CREATE TABLE `product` (
  `name` varchar(255) PRIMARY KEY,
  `description` varchar(255),
  `price` integer,
  `warranty_period` varchar(255),
  `supplier_name` varchar(255),
  `category_name` varchar(255)
);

CREATE TABLE `category` (
  `name` varchar(255) PRIMARY KEY
);

CREATE TABLE `supplier` (
  `name` varchar(255) PRIMARY KEY,
  `contact` varchar(255),
  `tel_number` integer,
  `email` varchar(255)
);

CREATE TABLE `customer` (
  `name` varchar(255) PRIMARY KEY,
  `surname` varchar(255),
  `tel_number` integer,
  `email` varchar(255)
);

CREATE TABLE `order` (
  `order_id` integer PRIMARY KEY,
  `product_name` varchar(255),
  `product_price` varchar(255),
  `customer_name` varchar(255),
  `status` varchar(255)
);

ALTER TABLE `supplier` ADD FOREIGN KEY (`name`) REFERENCES `product` (`supplier_name`);

ALTER TABLE `customer` ADD FOREIGN KEY (`name`) REFERENCES `order` (`customer_name`);

ALTER TABLE `product` ADD FOREIGN KEY (`category_name`) REFERENCES `category` (`name`);

ALTER TABLE `order` ADD FOREIGN KEY (`product_name`) REFERENCES `product` (`name`);

ALTER TABLE `order` ADD FOREIGN KEY (`product_price`) REFERENCES `product` (`price`);
