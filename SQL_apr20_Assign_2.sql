-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2023 at 01:02 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `task_apr20_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`name`) VALUES
('[accessories]'),
('[PCs]'),
('[portable computers]'),
('[softwares]');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `tel_number` varchar(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`name`, `surname`, `tel_number`, `email`) VALUES
('[Andris]', '[Bergs]', '[+371223344', '[a.bergs.test@gmail.com]'),
('[Anita]', '[Eglite]', '[+371223344', '[a.eglite.test@gmail.com]'),
('[Janis]', '[Berzins]', '[+371223344', '[j.berzins.test@gmail.com]');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `order_id` varchar(11) NOT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `product_price` varchar(255) DEFAULT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`order_id`, `product_name`, `product_price`, `customer_name`, `status`) VALUES
('[1001]', '[Lenovo ThinkPad T15g (Gen 1) 15.6]', '[3500]', '[Andris Bergs]', '[in processing]'),
('[1002]', '[Apple MacBook Pro 16]', '[4100]', '[Anita Eglite]', '[delivered and paid]'),
('[1003]', '[Dell XPS 17]', '[3900]', '[Janis Berzins]', '[entered]');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` varchar(11) DEFAULT NULL,
  `warranty_period` varchar(255) DEFAULT NULL,
  `supplier_name` varchar(255) DEFAULT NULL,
  `category_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`name`, `description`, `price`, `warranty_period`, `supplier_name`, `category_name`) VALUES
('Lenovo ThinkPad T15g (Gen 1) 15.6]', '[Portatīvais dators Lenovo ThinkPad T15g (Gen 1) 15.6\' Black 20UR003DMH]', '0', '[24 month]', '[SIA Euronics Latvia]', '[portable computers]'),
('[Apple MacBook Pro 16]', '[Portatīvais dators Apple MacBook Pro 16\" M2 Max 12-core CPU 38-core GPU 32GB 1TB SSD Space Gray ENG]', '0', '[24 month]', '[SIA Tet]', '[portable computers]'),
('[Dell XPS 17]', '[Portatīvais dators Dell XPS 17 9720 17]', '0', '[24 month]', '[SIA PIGU Latvia]', '[portable computers]');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `name` varchar(255) NOT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `tel_number` varchar(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`name`, `contact`, `tel_number`, `email`) VALUES
('[SIA Euronics Latvia]', '[Ieriķu iela 5B, Rīga, Latvija, LV-1084]', '[+371675558', '[klientu.centrs@euronics.lv]'),
('[SIA PIGU Latvia]', '[Maskavas iela 257, Rīga, Latvija, LV-1019]', '[+371252202', '[partneriams@220.lv]'),
('[SIA Tet]', '[Dzirnavu iela 105, Rīga, Latvija, LV-1011]', '[+371673337', '[tetveikals@tet.lv]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
