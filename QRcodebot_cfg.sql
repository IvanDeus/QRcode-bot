-- phpMyAdmin SQL Dump
-- https://www.phpmyadmin.net/
-- Server version: 8.0.37
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `QRcodebot`
--

-- --------------------------------------------------------

--
-- Table structure for table `telebot_users`
--

CREATE TABLE `telebot_users` (
  `id` int NOT NULL,
  `chat_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `lastupd` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lastmsg` text CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci,
  `Sub` tinyint(1) NOT NULL DEFAULT '0',
  `first_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `last_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `level` smallint DEFAULT '0',
  `email` varchar(222) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `phone` varchar(33) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `u_url` varchar(500) COLLATE utf8mb3_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `telebot_vars`
--

CREATE TABLE `telebot_vars` (
  `id` int NOT NULL,
  `param` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `value` varchar(3800) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

--
-- Dumping data for table `telebot_vars`
--

INSERT INTO `telebot_vars` (`id`, `param`, `value`) VALUES
(3, 'welcome_message', 'Press the \'Get QR\' button to generate an A4 format PDF for your URL.'),
(4, 'welcome_nostart', 'Sorry, I don\'t understand. Please ensure your prompt is correct and the title is not too long. Alternatively, press /start to restart the process.'),
(5, 'url_text', 'Enter your URL:'),
(6, 'titul_text', 'Enter document title:'),
(7, 'help', 'Help'),
(8, 'qr', 'Get QR'),
(9, 'gen_text', 'Generating QR code...'),
(10, 'gen_text_done', 'Done! Would you like to generate another?'),
(11, 'help_text', 'Instructions for creating a QR code: Ensure there are no empty spaces in your input. The URL should begin with http:// or https://. Both the title and URL can be in Cyrillic.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `telebot_users`
--
ALTER TABLE `telebot_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `telebot_vars`
--
ALTER TABLE `telebot_vars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `telebot_users`
--
ALTER TABLE `telebot_users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `telebot_vars`
--
ALTER TABLE `telebot_vars`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
