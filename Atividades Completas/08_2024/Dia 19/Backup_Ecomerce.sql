-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 10.28.2.36    Database: ecomerce
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `EX2_CLIENTE`
--

DROP TABLE IF EXISTS `EX2_CLIENTE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EX2_CLIENTE` (
  `cod_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `data_nascimento` date NOT NULL,
  `cpf` char(11) NOT NULL,
  PRIMARY KEY (`cod_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EX2_CLIENTE`
--

LOCK TABLES `EX2_CLIENTE` WRITE;
/*!40000 ALTER TABLE `EX2_CLIENTE` DISABLE KEYS */;
/*!40000 ALTER TABLE `EX2_CLIENTE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EX2_ITEMPEDIDO`
--

DROP TABLE IF EXISTS `EX2_ITEMPEDIDO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EX2_ITEMPEDIDO` (
  `cod_pedido` int NOT NULL,
  `cod_produto` int NOT NULL,
  `numero_item` int NOT NULL AUTO_INCREMENT,
  `volor_unitario` float NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`numero_item`),
  KEY `cod_pedido` (`cod_pedido`),
  KEY `cod_produto` (`cod_produto`),
  CONSTRAINT `EX2_ITEMPEDIDO_ibfk_1` FOREIGN KEY (`cod_pedido`) REFERENCES `EX2_PEDIDO` (`cod_pedido`),
  CONSTRAINT `EX2_ITEMPEDIDO_ibfk_2` FOREIGN KEY (`cod_produto`) REFERENCES `EX2_PRODUTO` (`cod_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EX2_ITEMPEDIDO`
--

LOCK TABLES `EX2_ITEMPEDIDO` WRITE;
/*!40000 ALTER TABLE `EX2_ITEMPEDIDO` DISABLE KEYS */;
/*!40000 ALTER TABLE `EX2_ITEMPEDIDO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EX2_LOG`
--

DROP TABLE IF EXISTS `EX2_LOG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EX2_LOG` (
  `cod_log` int NOT NULL AUTO_INCREMENT,
  `data_log` date NOT NULL,
  `descricao` varchar(255) NOT NULL,
  PRIMARY KEY (`cod_log`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EX2_LOG`
--

LOCK TABLES `EX2_LOG` WRITE;
/*!40000 ALTER TABLE `EX2_LOG` DISABLE KEYS */;
/*!40000 ALTER TABLE `EX2_LOG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EX2_PEDIDO`
--

DROP TABLE IF EXISTS `EX2_PEDIDO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EX2_PEDIDO` (
  `cod_pedido` int NOT NULL AUTO_INCREMENT,
  `cod_cliente` int NOT NULL,
  `data_pedido` date NOT NULL,
  `nota_fiscal` varchar(255) NOT NULL,
  `valor_total` float NOT NULL,
  PRIMARY KEY (`cod_pedido`),
  KEY `cod_cliente` (`cod_cliente`),
  CONSTRAINT `EX2_PEDIDO_ibfk_1` FOREIGN KEY (`cod_cliente`) REFERENCES `EX2_CLIENTE` (`cod_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EX2_PEDIDO`
--

LOCK TABLES `EX2_PEDIDO` WRITE;
/*!40000 ALTER TABLE `EX2_PEDIDO` DISABLE KEYS */;
/*!40000 ALTER TABLE `EX2_PEDIDO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EX2_PRODUTO`
--

DROP TABLE IF EXISTS `EX2_PRODUTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EX2_PRODUTO` (
  `cod_produto` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`cod_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EX2_PRODUTO`
--

LOCK TABLES `EX2_PRODUTO` WRITE;
/*!40000 ALTER TABLE `EX2_PRODUTO` DISABLE KEYS */;
/*!40000 ALTER TABLE `EX2_PRODUTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EX2_REQUISICAO_COMPRA`
--

DROP TABLE IF EXISTS `EX2_REQUISICAO_COMPRA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EX2_REQUISICAO_COMPRA` (
  `cod_requisicao_compra` int NOT NULL AUTO_INCREMENT,
  `cod_produto` int NOT NULL,
  `data_requisicao` date NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`cod_requisicao_compra`),
  KEY `cod_produto` (`cod_produto`),
  CONSTRAINT `EX2_REQUISICAO_COMPRA_ibfk_1` FOREIGN KEY (`cod_produto`) REFERENCES `EX2_ITEMPEDIDO` (`cod_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EX2_REQUISICAO_COMPRA`
--

LOCK TABLES `EX2_REQUISICAO_COMPRA` WRITE;
/*!40000 ALTER TABLE `EX2_REQUISICAO_COMPRA` DISABLE KEYS */;
/*!40000 ALTER TABLE `EX2_REQUISICAO_COMPRA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ecomerce'
--

--
-- Dumping routines for database 'ecomerce'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-19  9:01:53
