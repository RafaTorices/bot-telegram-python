-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.2.0 - MySQL Community Server - GPL
-- SO del servidor:              Linux
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para devops
CREATE DATABASE IF NOT EXISTS `devops` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `devops`;

-- Volcando estructura para tabla devops.estado
CREATE TABLE IF NOT EXISTS `estado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `estado` int DEFAULT '0',
  `notas` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- Volcando datos para la tabla devops.estado: ~1 rows (aproximadamente)

INSERT INTO `estado` (`id`, `updated`, `estado`, `notas`) VALUES
	(1, '2024-01-17 17:04:55', 0, 'MANTENIMIENTO');

-- Volcando estructura para tabla devops.opciones
CREATE TABLE IF NOT EXISTS `opciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `opcion` varchar(20) COLLATE utf8mb3_spanish_ci NOT NULL,
  `texto` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- Volcando datos para la tabla devops.opciones: ~4 rows (aproximadamente)

INSERT INTO `opciones` (`id`, `updated`, `opcion`, `texto`) VALUES
	(1, '2024-01-17 17:05:15', 'opcion1', 'Texto para opcion1'),
	(2, '2024-01-17 17:05:25', 'opcion2', 'Texto para opcion2'),
	(3, '2024-01-17 17:05:34', 'opcion3', 'Texto para opcion3'),
	(4, '2024-01-17 17:05:41', 'opcion4', 'Texto para opcion4');

-- Volcando estructura para tabla devops.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `first_name` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `chatid` varchar(20) COLLATE utf8mb3_spanish_ci NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `autorizado` int DEFAULT '0',
  `pendiente` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- Volcando datos para la tabla devops.usuarios: ~0 rows (aproximadamente)

-- Volcando estructura para tabla devops.mensajes
CREATE TABLE IF NOT EXISTS `mensajes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `updated` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
  `first_name` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `chatid` varchar(20) COLLATE utf8mb3_spanish_ci NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `mensaje` text COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;



/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
