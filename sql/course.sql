-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: course
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` varchar(10) NOT NULL,
  `user` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `logintime` datetime(6) DEFAULT NULL,
  `loginip` int(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area` (
  `id` varchar(10) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area_rule`
--

DROP TABLE IF EXISTS `area_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area_rule` (
  `id` varchar(10) NOT NULL,
  `area_id` varchar(10) DEFAULT NULL,
  `rule_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `area_id` (`area_id`),
  KEY `rule_id` (`rule_id`),
  CONSTRAINT `area_rule_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `area_rule_ibfk_2` FOREIGN KEY (`rule_id`) REFERENCES `rule` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_rule`
--

LOCK TABLES `area_rule` WRITE;
/*!40000 ALTER TABLE `area_rule` DISABLE KEYS */;
/*!40000 ALTER TABLE `area_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `id` varchar(10) NOT NULL,
  `date` datetime(6) DEFAULT NULL,
  `pic_path` varchar(255) DEFAULT NULL,
  `area_id` varchar(10) DEFAULT NULL,
  `vedio_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `area_id` (`area_id`),
  KEY `vedio_id` (`vedio_id`),
  CONSTRAINT `log_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `log_ibfk_2` FOREIGN KEY (`vedio_id`) REFERENCES `vedio` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rule`
--

DROP TABLE IF EXISTS `rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rule` (
  `id` varchar(10) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rule`
--

LOCK TABLES `rule` WRITE;
/*!40000 ALTER TABLE `rule` DISABLE KEYS */;
/*!40000 ALTER TABLE `rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rule_log`
--

DROP TABLE IF EXISTS `rule_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rule_log` (
  `id` varchar(10) NOT NULL,
  `rule_id` varchar(10) DEFAULT NULL,
  `log_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rule_id` (`rule_id`),
  KEY `log_id` (`log_id`),
  CONSTRAINT `rule_log_ibfk_1` FOREIGN KEY (`rule_id`) REFERENCES `rule` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `rule_log_ibfk_2` FOREIGN KEY (`log_id`) REFERENCES `log` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rule_log`
--

LOCK TABLES `rule_log` WRITE;
/*!40000 ALTER TABLE `rule_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `rule_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vedio`
--

DROP TABLE IF EXISTS `vedio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vedio` (
  `id` varchar(10) NOT NULL,
  `save_path` varchar(255) DEFAULT NULL,
  `area_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `area_id` (`area_id`),
  CONSTRAINT `vedio_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vedio`
--

LOCK TABLES `vedio` WRITE;
/*!40000 ALTER TABLE `vedio` DISABLE KEYS */;
/*!40000 ALTER TABLE `vedio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-17 12:18:12
