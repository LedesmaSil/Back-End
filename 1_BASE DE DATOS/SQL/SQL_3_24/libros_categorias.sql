-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 26, 2022 at 07:04 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `comision22538`
--

-- --------------------------------------------------------

--
-- Table structure for table `categorias`
--

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categorias`
--

INSERT INTO `categorias` (`id`, `nombre`) VALUES
(1, 'autoayuda'),
(2, 'cocina'),
(3, 'ficcion'),
(4, 'filosofia'),
(5, 'novela'),
(6, 'educacion'),
(7, 'poesia'),
(8, NULL),
(9, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `libros`
--

CREATE TABLE `libros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `autor` varchar(130) NOT NULL,
  `editorial` varchar(80) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` int(11) NOT NULL,
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `libros`
--

INSERT INTO `libros` (`id`, `nombre`, `autor`, `editorial`, `cantidad`, `precio`, `id_categoria`) VALUES
(1, 'El club de las 5 de la mañana', 'Robin S. Sharma', NULL, 35, 9000, 1),
(2, 'Como como', 'Natalia Kiako', NULL, 12, 5000, 2),
(3, 'El Aleph', 'Jorge Luis Borges', 'Losada', 22, 1000, 3),
(4, 'El ser y la nada', 'Jean Paul Sartre', 'Losada', 5, 800, 4),
(5, 'Emperador y Galileo', 'Henrik Ibsen', 'Losada', 2, 3000, 4),
(6, 'Ficciones', 'Jorge Luis Borges', 'Emecé Editores', 13, 2500, 3),
(7, 'Rayuela', 'Julio Cortazar', 'Sudamericana', 22, 5500, 5),
(8, '1984', 'George Orwell', NULL, 17, 4600, 3),
(9, 'Un mundo felix', 'Aldous Huxley', NULL, 11, 4270, 3),
(10, 'Harry Potter y la piedra filosofal', 'J. K. Rowling', NULL, 10, 14000, 3),
(11, 'Harry Potter y la camara secreta', 'J. K. Rowling', NULL, 10, 14000, 3),
(12, 'Harry Potter y el prisionero de Azkaban', 'J. K. Rowling', NULL, 10, 14000, 3),
(13, 'Harry Potter y el cáliz de fuego', 'J. K. Rowling', NULL, 10, 14000, 3),
(14, 'Harry Potter y la orden fel Féliz', 'J. K. Rowling', NULL, 10, 14000, 6),
(15, 'Harry Potter y el misterio del príncipe', 'J. K. Rowling', NULL, 10, 14000, 3),
(16, 'Harry Potter y las reliquias de la muerte', 'J. K. Rowling', NULL, 10, 14000, 3),
(17, 'El monje que vendio su ferrari', 'Robin S. Sharma', 'HarperCollins', 19, 5000, 3),
(18, 'Padre rico y padre pobre', 'Robert Kiyosaki', NULL, 7, 5050, 6),
(19, 'El Aleph', 'Jorge Luis Borges', 'Planeta', 15, 3470, 3),
(20, 'Martin Fierro', 'Jode Hernandez', 'Emece', 22, 4800, 7),
(21, 'Antología poética', 'Jorge Luis Borges', 'Planeta', 9, 1700, 7),
(22, 'Aprenda PHP', 'Mario Molina', 'Emece', 7, 2500, 6),
(23, 'Cervantes y el Quijote', 'Jorge Luis Borges', 'Paidos', 4, 3700, 8),
(24, 'Manual de PHP', 'J. C. Paez', 'Paidos', 12, 5120, NULL),
(25, 'Alicia en el País de las Maravillas', 'Lewis Carroll', 'Paidos', 11, 2900, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
