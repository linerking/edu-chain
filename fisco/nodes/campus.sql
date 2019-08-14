-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: campus
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.16.04.1

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
-- Table structure for table `tab_certificate`
--

DROP TABLE IF EXISTS `tab_certificate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_certificate` (
  `index_id` int(11) NOT NULL AUTO_INCREMENT,
  `certificate_id` varchar(100) NOT NULL,
  PRIMARY KEY (`index_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_certificate`
--

LOCK TABLES `tab_certificate` WRITE;
/*!40000 ALTER TABLE `tab_certificate` DISABLE KEYS */;
/*!40000 ALTER TABLE `tab_certificate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tab_stud_basic_info`
--

DROP TABLE IF EXISTS `tab_stud_basic_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_stud_basic_info` (
  `index_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `grade` int(11) NOT NULL,
  `major` varchar(100) NOT NULL,
  PRIMARY KEY (`index_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_stud_basic_info`
--

LOCK TABLES `tab_stud_basic_info` WRITE;
/*!40000 ALTER TABLE `tab_stud_basic_info` DISABLE KEYS */;
INSERT INTO `tab_stud_basic_info` VALUES (1,'stud1',NULL,2,'cse'),(2,'stud2',NULL,1,'cse'),(3,'stud3',NULL,1,'cse'),(4,'stud4',NULL,1,'cse'),(5,'stud5',NULL,1,'cse'),(6,'stud6',NULL,1,'cse'),(7,'stud7',NULL,4,'cse'),(8,'stud8',NULL,3,'cse'),(9,'stud9',NULL,3,'cse'),(10,'stud10',NULL,3,'cse');
/*!40000 ALTER TABLE `tab_stud_basic_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tab_stud_course_info`
--

DROP TABLE IF EXISTS `tab_stud_course_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_stud_course_info` (
  `index_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `course_code` varchar(100) NOT NULL,
  `grades` int(11) DEFAULT NULL,
  `teacher_name` varchar(100) NOT NULL,
  `semester` varchar(100) DEFAULT NULL,
  `student_name` varchar(100) NOT NULL,
  PRIMARY KEY (`index_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_stud_course_info`
--

LOCK TABLES `tab_stud_course_info` WRITE;
/*!40000 ALTER TABLE `tab_stud_course_info` DISABLE KEYS */;
INSERT INTO `tab_stud_course_info` VALUES (1,NULL,'csc1001',78,'tchr1',NULL,'stud1'),(2,NULL,'csc1001',72,'tchr1',NULL,'stud2'),(3,NULL,'csc1001',75,'tchr1',NULL,'stud3'),(4,NULL,'csc1001',99,'tchr1',NULL,'stud4'),(5,NULL,'csc3001',19,'tchr2',NULL,'stud5'),(6,NULL,'csc3001',49,'tchr2',NULL,'stud6'),(7,NULL,'csc3001',76,'tchr2',NULL,'stud7'),(8,NULL,'csc3010',87,'tchr3',NULL,'stud8'),(9,NULL,'csc3010',89,'tchr3',NULL,'stud9'),(10,NULL,'csc3010',92,'tchr3',NULL,'stud10');
/*!40000 ALTER TABLE `tab_stud_course_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tab_tchr_basic_info`
--

DROP TABLE IF EXISTS `tab_tchr_basic_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_tchr_basic_info` (
  `index_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`index_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_tchr_basic_info`
--

LOCK TABLES `tab_tchr_basic_info` WRITE;
/*!40000 ALTER TABLE `tab_tchr_basic_info` DISABLE KEYS */;
INSERT INTO `tab_tchr_basic_info` VALUES (1,'tchr1',NULL,'professor'),(2,'tchr2',NULL,'professor'),(3,'tchr3',NULL,'professor');
/*!40000 ALTER TABLE `tab_tchr_basic_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tab_tchr_course_info`
--

DROP TABLE IF EXISTS `tab_tchr_course_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tab_tchr_course_info` (
  `index_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `course_code` varchar(100) NOT NULL,
  `semester` varchar(100) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`index_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tab_tchr_course_info`
--

LOCK TABLES `tab_tchr_course_info` WRITE;
/*!40000 ALTER TABLE `tab_tchr_course_info` DISABLE KEYS */;
INSERT INTO `tab_tchr_course_info` VALUES (1,NULL,'csc1001',NULL,'tchr1'),(2,NULL,'csc3001',NULL,'tchr2'),(3,NULL,'csc3010',NULL,'tchr3');
/*!40000 ALTER TABLE `tab_tchr_course_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-12 23:02:30
