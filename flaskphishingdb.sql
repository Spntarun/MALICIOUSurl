-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2023 at 01:20 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskphishingdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `Uid` varchar(50) NOT NULL,
  `Uname` varchar(80) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Pswd` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Addr` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`Uid`, `Uname`, `Name`, `Pswd`, `Email`, `Phone`, `Addr`) VALUES
('User70808', 'dd', 'Surya A Naragund', 'qazwsx', 'kavanaravi1@gmail.com', 'Mysore', 'Mysore'),
('User82829', 'San', 'Surya', 'surya1998', 'surya.a.naragund@gmail.com', '#16/9 \"surya\" sjc road k.r.nagar', '#16/9 \"surya\" sjc road k.r.nagar'),
('User16429', 'Demo', 'Demo', 'qazwsx', 'demo@gmail.com', 'Mysore', 'Mysore'),
('User24321', 'Demo', 'Demo', 'qazwsx', 'demo@gmail.com', 'Mysore', 'Mysore'),
('User77340', 'Demo', 'Demo', 'qazwsx', 'demo@gmail.com', 'Mysore', 'Mysore'),
('User93264', 'Tarun', 'N', 'qazwsx', 'tarun@gmail.com', 'asdfhk', 'asdfhk'),
('User97378', 'Lathamani', 'Lathamani', '8296649213', 'manilatha353@gmail.com', 'Mandya', 'Mandya'),
('User24613', 'madhupriya R K', 'madhu', '968604406', 'madhu@gmail.com', 'Mysore', 'Mysore'),
('User67548', 'Kampana', 'Kampana C V', '1324', 'kampu@gmail.com', 'Hasana', 'Hasana');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
