-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
-- Server version: 8.0
-- PHP Version: 7.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

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
  `lastmsg` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `Sub` tinyint(1) NOT NULL DEFAULT '0',
  `first_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `last_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `level` smallint DEFAULT '0',
  `email` varchar(222) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `phone` varchar(33) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `u_url` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL DEFAULT '__'
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
(3, 'welcome_message', 'Создайте QR-код на любой линк! \r\nПросто нажмите \'Get QR\' и введите свою ссылку.\r\n\r\nPress the \'Get QR\' button to generate an A4 format PDF for your URL.'),
(4, 'welcome_nostart', 'Извините, не понимаю. Пожалуйста, убедитесь, что ссылка без кавычек и пробелов, и заголовок не слишком длинный. Либо нажмите /start, чтобы перезапустить процесс.\r\n\r\nSorry, I don\'t understand. Please ensure your prompt is correct and the title is not too long. Alternatively, press /start to restart the process.'),
(5, 'url_text', 'Вставьте свою ссылку:\r\n\r\nEnter your URL:'),
(6, 'titul_text', 'Напишите заголовок:\r\n\r\nEnter document title:'),
(7, 'help', 'Help'),
(8, 'qr', 'Get QR'),
(9, 'gen_text', 'Генерирую... \r\n\r\nGenerating QR code...'),
(10, 'gen_text_done', 'Готово! Ещё? Если нравится бот, <i>присылайте донаты на криптокошелёк Toncoin/Notcoin/USDT (TON):</i><b> UQAM8RmCrA5_R1Bw8uFJ0imW6OfupgGxvedbYoaIIdONZ447\r\n</b>\r\nDone! More? If you like this bot, <i>please donate  Toncoin/Notcoin/USDT (TON):</i><b> UQAM8RmCrA5_R1Bw8uFJ0imW6OfupgGxvedbYoaIIdONZ447\r\n</b>'),
(11, 'help_text', 'Как создать QR-код в формате А4? Убедитесь, что при вводе ссылки нет пустых мест, пропусков, пробелов. Линк (cсылка, URL) должен начинаться с http:// или https://. И заголовок (может быть с пробелами), и URL-адрес могут быть написаны кириллицей.\r\n\r\nInstructions for creating a QR code: Ensure there are no empty spaces in your input. The URL should begin with http:// or https://. Both the title and URL can be in Cyrillic.');

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
