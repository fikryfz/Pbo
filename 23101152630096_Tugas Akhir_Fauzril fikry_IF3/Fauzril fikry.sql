-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Jan 2025 pada 19.26
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_motor_fikry`
--
CREATE DATABASE IF NOT EXISTS `db_motor_fikry` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_motor_fikry`;

-- --------------------------------------------------------

--
-- Struktur dari tabel `customers_fikry`
--

CREATE TABLE `customers_fikry` (
  `cust_id` int(11) NOT NULL,
  `cust_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `customers_fikry`
--

INSERT INTO `customers_fikry` (`cust_id`, `cust_name`) VALUES
(2, 'Rifki ahmad'),
(3, 'Rizky hamzary'),
(8, 'Fauzril fikry');

-- --------------------------------------------------------

--
-- Struktur dari tabel `orders_fikry`
--

CREATE TABLE `orders_fikry` (
  `id_order` int(11) NOT NULL,
  `cust_id` int(11) DEFAULT NULL,
  `id_product` int(11) DEFAULT NULL,
  `order_date` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `total` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `orders_fikry`
--

INSERT INTO `orders_fikry` (`id_order`, `cust_id`, `id_product`, `order_date`, `quantity`, `total`) VALUES
(1, 2, 1, '2025-01-25 01:22:14', 2, 64000000.00);

-- --------------------------------------------------------

--
-- Struktur dari tabel `products_fikry`
--

CREATE TABLE `products_fikry` (
  `id_product` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` decimal(15,2) NOT NULL,
  `product_type` enum('motorcycle','electric') NOT NULL,
  `cylinder` int(11) DEFAULT NULL,
  `tank_capacity` float DEFAULT NULL,
  `battery` int(11) DEFAULT NULL,
  `mileage` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `products_fikry`
--

INSERT INTO `products_fikry` (`id_product`, `name`, `price`, `product_type`, `cylinder`, `tank_capacity`, `battery`, `mileage`) VALUES
(1, 'Nmax 120', 32000000.00, 'motorcycle', 100, 15, NULL, NULL),
(2, 'Klx', 31000000.00, 'motorcycle', 120, 20, NULL, NULL),
(3, 'Beat street', 18000000.00, 'motorcycle', 90, 10, NULL, NULL),
(4, 'Fero', 4000000.00, 'electric', NULL, NULL, 17, 120),
(6, 'sepeda', 40000000.00, 'motorcycle', 150, 20, NULL, NULL),
(7, 'Wuling motor', 3000000.00, 'electric', NULL, NULL, 100, 10);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `customers_fikry`
--
ALTER TABLE `customers_fikry`
  ADD PRIMARY KEY (`cust_id`);

--
-- Indeks untuk tabel `orders_fikry`
--
ALTER TABLE `orders_fikry`
  ADD PRIMARY KEY (`id_order`),
  ADD KEY `cust_id` (`cust_id`),
  ADD KEY `id_product` (`id_product`);

--
-- Indeks untuk tabel `products_fikry`
--
ALTER TABLE `products_fikry`
  ADD PRIMARY KEY (`id_product`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `orders_fikry`
--
ALTER TABLE `orders_fikry`
  ADD CONSTRAINT `orders_fikry_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `customers_fikry` (`cust_id`),
  ADD CONSTRAINT `orders_fikry_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `products_fikry` (`id_product`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
