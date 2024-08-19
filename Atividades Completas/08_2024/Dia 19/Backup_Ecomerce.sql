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
  `codcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `datanascimento` date NOT NULL,
  `cpf` char(11) NOT NULL,
  PRIMARY KEY (`codcliente`)
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
  `codpedido` int NOT NULL,
  `codproduto` int NOT NULL,
  `numeroitem` int NOT NULL AUTO_INCREMENT,
  `volorunitario` float NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`numeroitem`),
  KEY `codpedido` (`codpedido`),
  KEY `codproduto` (`codproduto`),
  CONSTRAINT `EX2_ITEMPEDIDO_ibfk_1` FOREIGN KEY (`codpedido`) REFERENCES `EX2_PEDIDO` (`codpedido`),
  CONSTRAINT `EX2_ITEMPEDIDO_ibfk_2` FOREIGN KEY (`codproduto`) REFERENCES `EX2_PRODUTO` (`codproduto`)
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
  `codlog` int NOT NULL AUTO_INCREMENT,
  `data` date NOT NULL,
  `descricao` varchar(255) NOT NULL,
  PRIMARY KEY (`codlog`)
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
  `codpedido` int NOT NULL AUTO_INCREMENT,
  `codcliente` int NOT NULL,
  `datapedido` date NOT NULL,
  `notafiscal` varchar(255) NOT NULL,
  `valortotal` float NOT NULL,
  PRIMARY KEY (`codpedido`),
  KEY `codcliente` (`codcliente`),
  CONSTRAINT `EX2_PEDIDO_ibfk_1` FOREIGN KEY (`codcliente`) REFERENCES `EX2_CLIENTE` (`codcliente`)
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
  `codproduto` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`codproduto`)
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
  `codrequisicaocompra` int NOT NULL AUTO_INCREMENT,
  `codproduto` int NOT NULL,
  `data` date NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`codrequisicaocompra`),
  KEY `codproduto` (`codproduto`),
  CONSTRAINT `EX2_REQUISICAO_COMPRA_ibfk_1` FOREIGN KEY (`codproduto`) REFERENCES `EX2_ITEMPEDIDO` (`codproduto`)
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

-- Dump completed on 2024-08-19  9:26:28
