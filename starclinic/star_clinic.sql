-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2026 at 05:18 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `star_clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('dc5f5277ae51');

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `id` int(11) NOT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `appointment_schedule` datetime NOT NULL,
  `reason` text NOT NULL,
  `status` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `consultation_fee` decimal(12,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`id`, `patient_id`, `doctor_id`, `appointment_schedule`, `reason`, `status`, `created_at`, `consultation_fee`) VALUES
(1, 2, 20, '2026-10-08 16:00:00', 'Ask me again😂😂', 'Pending', '2026-10-06 20:45:02', 0.00),
(2, 2, 22, '2026-10-01 10:00:00', '............................', 'Completed', '2026-10-07 08:38:31', 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `specialty_id` int(11) DEFAULT NULL,
  `availability` varchar(50) NOT NULL,
  `licence_number` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `first_name`, `last_name`, `email`, `phone`, `specialty_id`, `availability`, `licence_number`, `created_at`, `user_id`) VALUES
(20, 'Daisy', 'Chukwu', 'daisy38@gmail.com', '09126741114', 2, 'Monday - Friday', 'BTC001', '2026-10-06 20:42:30', 3),
(21, 'Lateef', 'Sakariyau', 'oluwatiseajose15@gmail.com', '09066429731', 5, 'Monday - wednesday', 'BTC004', '2026-10-07 06:56:05', 5),
(22, 'Naomi', 'Naomi', 'naomi@gmail.com', '09066429731', 1, 'Monday - Friday', 'BTC008', '2026-10-07 08:35:36', 6);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `first_name`, `last_name`, `email`, `phone`, `user_id`) VALUES
(1, 'Peter', 'Parker', 'oluwatiseajose3@gmail.com', '09073681455', 2),
(2, 'Tony', 'Stark', 'oluwatiseajose18@gmail.com', '09024355028', 4);

-- --------------------------------------------------------

--
-- Table structure for table `specialty`
--

CREATE TABLE `specialty` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `specialty`
--

INSERT INTO `specialty` (`id`, `name`, `description`, `created_at`) VALUES
(1, 'Cardiology', 'Treatment of heart.', '2026-09-26 10:59:50'),
(2, 'Dermatology', 'Treatment of skin conditions.', '2026-09-26 10:59:50'),
(3, 'Paediatrics', 'Medical care for kids.', '2026-09-26 10:59:50'),
(4, 'General Medicine', 'General medical care and treatment.', '2026-09-26 10:59:50'),
(5, 'Orthopaedics', 'Treatment of bones, joints and muscles.', '2026-09-26 10:59:50');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `role` varchar(20) NOT NULL DEFAULT 'patient'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `phone`, `password`, `created_at`, `role`) VALUES
(1, 'Oluwatise', 'Ajose', 'oluwatiseajose38@gmail.com', '09073681455', 'scrypt:32768:8:1$q5hh2dvJ1GrpPS3G$cb4386e2d09a840e251a8af8ec4b813c06eb20a20575d807ccf5a126d744b9eec60bd6fad4c79a024a21a2bfd90538404b12202ba5385ee71a35b5255f850055', '2026-10-05 12:40:25', 'patient'),
(2, 'Peter', 'Parker', 'oluwatiseajose3@gmail.com', '09073681455', 'scrypt:32768:8:1$vHA8cRY7DrP9t1xp$4f8f26c5199eb1e1d6c94901f2f6713d7092a8bb5dae2f84b15dac2591a1ae3376155869d091be3cdc92a8899897155c48bdfbaad9d017620f7cd8a790b8b891', '2026-10-06 20:08:50', 'admin'),
(3, 'Daisy', 'Chukwu', 'daisy38@gmail.com', '09126741114', 'scrypt:32768:8:1$qnwXnjLiO9VgN3da$1c34e0a435e09f037ac693820f7e5d621c1374c0dae5b1b6f2425856ab7de792e6dcd280db1f9a69bfc8e5b6a18ab6390d5a2bea62b0e02156a94ff8889396fd', '2026-10-06 20:42:30', 'doctor'),
(4, 'Tony', 'Stark', 'oluwatiseajose18@gmail.com', '09024355028', 'scrypt:32768:8:1$hv8FIFtj0C4aI3hr$0b1715219c3150ab4fc74d3458bea653bd9672798b981fdfe3eb512970ea8d6a8c694139a7c549b37c3fbc162c36a819a8d39147225e1219c36e4fb20216cd4f', '2026-10-06 20:43:53', 'patient'),
(5, 'Lateef', 'Sakariyau', 'oluwatiseajose15@gmail.com', '09066429731', 'scrypt:32768:8:1$9f0638kp0ezScRNt$f0be25fb596fea2029f42b121231c84b1094a35ccee70f01be1a4e27efadc6b336b3ffa5166a6d7264033370c3abdabea8f7854125d988a0b3b0ee7cc9967b77', '2026-10-07 06:56:05', 'doctor'),
(6, 'Naomi', 'Naomi', 'naomi@gmail.com', '09066429731', 'scrypt:32768:8:1$HKQys61w7TWRXDNJ$9fc3a00dae3f2af7437382969a5c43666026ab5465be32b03eb54dbfb9c9ae64673106647c4ff03360e7e2bba9a28fcdf808b4aa798b77cb55db33c6276bb553', '2026-10-07 08:35:36', 'doctor');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_id` (`doctor_id`),
  ADD KEY `patient_id` (`patient_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_doctor_user_id` (`user_id`),
  ADD KEY `specialty_id` (`specialty_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_patient_user_id` (`user_id`);

--
-- Indexes for table `specialty`
--
ALTER TABLE `specialty`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `specialty`
--
ALTER TABLE `specialty`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`id`),
  ADD CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`id`);

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`specialty_id`) REFERENCES `specialty` (`id`),
  ADD CONSTRAINT `fk_doctor_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `fk_patient_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
