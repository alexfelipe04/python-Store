CREATE DATABASE   BackEnd_Store; 
USE BackEnd_Store;


CREATE TABLE `categories` (
  `idcategories` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` tinyint DEFAULT NULL,
  PRIMARY KEY (`idcategories`)
);

CREATE TABLE `providers` (
  `idproviders` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `full_address` varchar(255) DEFAULT NULL,
  `providerscol` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` tinyint DEFAULT NULL,
  PRIMARY KEY (`idproviders`)
);




CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_category_id_idx` (`category_id`),
  CONSTRAINT `FK_category_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`idcategories`)
);

CREATE TABLE `purchase_orders` (
  `provider_id` int DEFAULT NULL,
  `date` timestamp NULL DEFAULT NULL,
  `total` decimal(10,0) unsigned DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` tinyint DEFAULT NULL,
  `id_purchase_orders` int NOT NULL,
  PRIMARY KEY (`id_purchase_orders`),
  KEY `FK_provider_id` (`provider_id`),
  CONSTRAINT `FK_provider_id` FOREIGN KEY (`provider_id`) REFERENCES `providers` (`idproviders`)
) ;


CREATE TABLE `purchase_order_detail` (
  `purchase_order_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int unsigned DEFAULT NULL,
  `total` decimal(10,0) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` tinyint DEFAULT NULL,
  KEY `FK_product_id_idx` (`product_id`),
  KEY `FK_purchase_order_idl` (`purchase_order_id`),
  CONSTRAINT `FK_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `FK_purchase_order_idl` FOREIGN KEY (`purchase_order_id`) REFERENCES `purchase_orders` (`id_purchase_orders`)
);



