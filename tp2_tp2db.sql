-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: tp2db
-- ------------------------------------------------------
-- Server version	5.7.11-log

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
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `ISBN` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `year` int(4) DEFAULT NULL,
  `edition` int(2) DEFAULT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (10026274,'Extremely Loud and Incredibly Close',1931,1),(10473662,'Don\'t Bend Over in the Garden, Granny, You Know Them Taters Got Eyes',1930,1),(11524160,'Alexander and the Terrible, Horrible, No Good, Very Bad Day',1943,1),(11633650,'the Particular Sadness of Lemon Cake',2000,1),(11775668,'Well-Behaved Women Seldom Make History',1997,1),(11822367,'Send More Idiots',1904,1),(13172789,'Nostradamus Ate My Hamster',1975,1),(14641702,'Tinker, Tailor, Soldier, Spy',1925,1),(17603912,'The Effect of Gamma Rays on Man-in-the-Moon Marigolds',1906,1),(18572283,'The Devil Wears Prada',2004,1),(18772124,'The Man Who Was Thursday: A Nightmare',1963,1),(18897729,'All Quiet on the Western Front',1935,1),(20722517,'One Hundred Years of Solitude',1909,1),(22342301,'I Have No Mouth and I Must Scream',2000,1),(23170196,'The Unbearable Lightness of Being',1985,1),(23508706,'When You Are Engulfed in Flames',2010,1),(24562594,'The Lone Ranger and Tonto Fistfight in Heaven',2000,1),(24905123,'If on a Winter\'s Night a Traveller',1934,1),(25890836,'I Capture the Castle',1986,1),(26770519,'Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values',1947,1),(26799126,'Are You There, Vodka? It\'s Me, Chelsea',1922,1),(29409437,'Neverwhere',1956,1),(29992729,'I Still Miss My Man But My Aim Is Getting Better',1943,1),(33394467,'The Zombie Survival Guide: Complete Protection from the Living Dead',1983,1),(35700201,'The Importance of Being Earnest',1976,1),(36481724,'No Country For Old Men',1931,1),(36690904,'An Arsonist\'s Guide to Writers\' Homes in New England',1961,1),(37039878,'The Spy Who Came In from the Cold',1969,1),(38149366,'The Long Dark Tea-Time of the Soul',1914,1),(38401616,'Fear and Loathing in Las Vegas',1953,1),(38548668,'John Dies at the End',1909,1),(41371466,'The Curious Incident of the Dog in the Night-Time',1979,1),(43488136,'Me Talk Pretty One Day',1935,1),(45452449,'Of Mice and Men',1942,1),(47390462,'How to Shit in the Woods: An Environmentally Sound Approach to a Lost Art',1983,1),(47706971,'How to Talk About Books You Haven\'t Read',1928,1),(49512337,'The Restaurant at the End of the Universe',1975,1),(51372721,'Stop Dressing Your Six-Year-Old Like a Skank: A Slightly Tarnished Southern Belle\'s Words of Wisdom',1907,1),(52799382,'Do Androids Dream of Electric Sheep?',1973,1),(53001908,'The Earth, My Butt, and Other Big Round Things',1922,1),(53251929,'The Man Without Qualities',1980,1),(54495733,'The Guernsey Literary and Potato Peel Pie Society',1933,1),(54956525,'For Whom the Bell Tolls',1974,1),(55334053,'A Confederacy of Dunces',1917,1),(57101159,'The Man Who Mistook His Wife for a Hat and Other Clinical Tales',1938,1),(58209935,'The Hitchhiker\'s Guide to the Galaxy',2008,1),(60725861,'The Grapes of Wrath',1971,1),(63722691,'How to Lose Friends and Alienate People',1967,1),(63830630,'And Then There Were None',1932,1),(64149464,'The Electric Kool-Aid Acid Test',1960,1),(64205116,'The Gordonston Ladies Dog Walking Club',1998,1),(64494248,'Cloudy With a Chance of Meatballs',1978,1),(65594252,'In God We Trust: All Others Pay Cash',1960,1),(65824440,'To Kill a Mockingbird',1900,1),(66269722,'I Was Told There\'d Be Cake',1948,1),(66493191,'The Silence of the Lambs',1930,1),(67348677,'As I Lay Dying',1998,1),(68676944,'A Heartbreaking Work of Staggering Genius',1962,1),(69111021,'Sense and Sensibility and Sea Monsters',1991,1),(70066210,'Brave New World',1948,1),(70174657,'Midnight in the Garden of Good and Evil: A Savannah Story',1971,1),(70413094,'Another Bullshit Night in Suck City',1929,1),(70445485,'Hard-Boiled Wonderland and the End of the World',1935,1),(70568046,'The Perks of Being a Wallflower',2008,1),(70737154,'The Lust Lizard of Melancholy Cove',1937,1),(70920498,'Love in the Time of Cholera',2005,1),(71742899,'A Clockwork Orange',1934,1),(73738012,'What to Say When You Talk to Yourself',1954,1),(74229475,'Pride and Prejudice and Zombies',1918,1),(74843713,'The Hollow Chocolate Bunnies of the Apocalypse',1921,1),(75737419,'The Lord of the Rings',1903,1),(76510972,'A Thousand Splendid Suns',1910,1),(77800151,'Dogshit Saved My Life',1963,1),(77825120,'Their Eyes Were Watching God',1900,1),(78146652,'Don\'t Pee on My Leg and Tell Me It\'s Raining: America\'s Toughest Family Court Judge Speaks Out',2000,1),(78455438,'A Short History of Tractors in Ukrainian',1912,1),(79623557,'The Sound and the Fury',1971,1),(82531446,'Where the Wild Things Are',1957,1),(82611330,'Captain Underpants and the Perilous Plot of Professor Poopypants',2005,1),(82638242,'There\'s a Wocket in My Pocket!',1929,1),(84711123,'Eats, Shoots & Leaves: The Zero Tolerance Approach to Punctuation',1949,1),(85273876,'Something Wicked This Way Comes',1983,1),(88319942,'The Moon is a Harsh Mistress',1942,1),(88749714,'Tequila Makes Her Clothes Fall Off',1938,1),(89934950,'The Catcher in the Rye',1904,1),(90117055,'So Long, and Thanks for All the Fish',1908,1),(94502125,'Life, the Universe and Everything',1933,1),(94632193,'I Hope They Serve Beer in Hell',1942,1),(95846251,'Livre de Test C++',2016,1),(96478058,'A Wrinkle in Time',1939,1),(97316790,'She Got Up Off The Couch: And Other Heroic Acts From Mooreland, Indiana',2006,1),(97892953,'This Is Not a Novel',1989,1),(99287393,'I Am America',1982,1);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_copy`
--

DROP TABLE IF EXISTS `book_copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book_copy` (
  `copyNo` int(4) NOT NULL AUTO_INCREMENT,
  `ISBN` int(4) NOT NULL,
  `available` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`copyNo`),
  KEY `ISBN` (`ISBN`),
  CONSTRAINT `book_copy_ibfk_1` FOREIGN KEY (`ISBN`) REFERENCES `book` (`ISBN`)
) ENGINE=InnoDB AUTO_INCREMENT=1145 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_copy`
--

LOCK TABLES `book_copy` WRITE;
/*!40000 ALTER TABLE `book_copy` DISABLE KEYS */;
INSERT INTO `book_copy` VALUES (1000,52799382,1),(1001,85273876,1),(1002,85273876,1),(1003,58209935,1),(1004,58209935,1),(1005,74229475,1),(1006,74229475,1),(1007,66269722,1),(1008,66269722,1),(1009,41371466,1),(1010,41371466,1),(1011,74843713,1),(1012,84711123,1),(1013,65824440,1),(1014,65824440,1),(1015,26799126,1),(1016,26799126,1),(1017,23170196,1),(1018,70174657,1),(1019,70568046,1),(1020,53001908,1),(1021,53001908,1),(1022,64494248,1),(1023,64494248,1),(1024,51372721,1),(1025,51372721,1),(1026,43488136,1),(1027,43488136,1),(1028,20722517,1),(1029,38149366,1),(1030,38149366,1),(1031,38548668,1),(1032,38548668,1),(1033,82531446,1),(1034,82531446,1),(1035,68676944,1),(1036,36690904,1),(1037,53251929,1),(1038,11524160,1),(1039,70413094,1),(1040,63722691,1),(1041,64205116,1),(1042,64205116,1),(1043,90117055,1),(1044,90117055,1),(1045,33394467,1),(1046,71742899,1),(1047,71742899,1),(1048,99287393,1),(1049,99287393,1),(1050,29409437,1),(1051,29409437,1),(1052,10026274,1),(1053,22342301,1),(1054,22342301,1),(1055,18572283,1),(1056,23508706,1),(1057,76510972,1),(1058,76510972,1),(1059,29992729,1),(1060,77825120,1),(1061,54495733,1),(1062,54495733,1),(1063,55334053,1),(1064,55334053,1),(1065,60725861,1),(1066,60725861,1),(1067,66493191,1),(1068,96478058,1),(1069,88749714,1),(1070,57101159,1),(1071,54956525,1),(1072,54956525,1),(1073,26770519,1),(1074,26770519,1),(1075,38401616,1),(1076,38401616,1),(1077,47390462,1),(1078,47390462,1),(1079,70920498,1),(1080,70920498,1),(1081,11822367,1),(1082,11822367,1),(1083,24905123,1),(1084,49512337,1),(1085,70066210,1),(1086,18772124,1),(1087,18772124,1),(1088,36481724,1),(1089,36481724,1),(1090,18897729,1),(1091,79623557,1),(1092,79623557,1),(1093,89934950,1),(1094,37039878,1),(1095,94632193,1),(1096,64149464,1),(1097,24562594,1),(1098,63830630,1),(1099,73738012,1),(1100,78146652,1),(1101,78146652,1),(1102,88319942,1),(1103,88319942,1),(1104,11775668,1),(1105,11775668,1),(1106,11633650,1),(1107,13172789,1),(1108,75737419,1),(1109,75737419,1),(1110,65594252,1),(1111,65594252,1),(1112,97316790,1),(1113,97316790,1),(1114,45452449,1),(1115,45452449,1),(1116,67348677,1),(1117,94502125,1),(1118,94502125,1),(1119,17603912,1),(1120,17603912,1),(1121,70445485,1),(1122,25890836,1),(1123,25890836,1),(1124,97892953,1),(1125,10473662,1),(1126,10473662,1),(1127,69111021,1),(1128,69111021,1),(1129,78455438,1),(1130,78455438,1),(1131,82611330,1),(1132,47706971,1),(1133,47706971,1),(1134,35700201,1),(1135,35700201,1),(1136,14641702,1),(1137,14641702,1),(1138,77800151,1),(1139,70737154,1),(1140,82638242,1),(1141,82638242,1),(1143,95846251,1),(1144,95846251,1);
/*!40000 ALTER TABLE `book_copy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookloan`
--

DROP TABLE IF EXISTS `bookloan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookloan` (
  `copyNo` int(4) NOT NULL,
  `dateOut` date NOT NULL,
  `dateDue` date NOT NULL,
  `borrowerNo` int(4) NOT NULL,
  PRIMARY KEY (`copyNo`,`dateOut`),
  KEY `borrowerNo` (`borrowerNo`),
  CONSTRAINT `bookloan_ibfk_1` FOREIGN KEY (`copyNo`) REFERENCES `book_copy` (`copyNo`),
  CONSTRAINT `bookloan_ibfk_2` FOREIGN KEY (`borrowerNo`) REFERENCES `borrower` (`borrowerNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookloan`
--

LOCK TABLES `bookloan` WRITE;
/*!40000 ALTER TABLE `bookloan` DISABLE KEYS */;
INSERT INTO `bookloan` VALUES (1000,'2015-11-06','2015-11-13',964),(1001,'2015-01-08','2015-01-16',211),(1001,'2015-09-17','2015-09-23',692),(1002,'2015-04-16','2015-04-24',874),(1002,'2015-12-04','2015-12-12',420),(1003,'2015-09-04','2015-09-12',304),(1003,'2015-09-18','2015-10-01',738),(1004,'2015-12-15','2015-12-25',319),(1006,'2015-05-23','2015-06-03',647),(1007,'2015-08-24','2015-09-03',523),(1008,'2015-03-15','2015-03-26',894),(1009,'2015-11-22','2015-12-02',631),(1010,'2015-01-15','2015-01-23',713),(1012,'2015-06-07','2015-06-12',761),(1012,'2015-11-28','2015-12-04',552),(1015,'2015-02-12','2015-02-22',873),(1015,'2015-02-20','2015-02-28',209),(1015,'2015-03-25','2015-04-04',959),(1016,'2015-04-06','2015-04-17',420),(1017,'2015-02-03','2015-02-15',589),(1017,'2015-03-18','2015-03-26',729),(1018,'2015-08-09','2015-08-17',873),(1018,'2015-09-17','2015-09-30',560),(1018,'2015-10-16','2015-10-26',729),(1019,'2015-07-26','2015-08-04',973),(1020,'2015-04-28','2015-05-03',390),(1021,'2015-09-08','2015-09-15',870),(1022,'2015-05-07','2015-05-15',915),(1023,'2015-04-12','2015-04-25',552),(1024,'2015-01-19','2015-02-02',170),(1024,'2015-08-26','2015-09-06',761),(1024,'2015-09-29','2015-10-08',319),(1024,'2015-11-02','2015-11-16',277),(1026,'2015-02-17','2015-02-26',272),(1026,'2015-06-10','2015-06-20',172),(1026,'2015-08-28','2015-09-06',247),(1026,'2015-09-06','2015-09-20',738),(1027,'2015-01-13','2015-01-22',232),(1027,'2015-02-09','2015-02-16',232),(1027,'2015-10-21','2015-10-28',272),(1027,'2015-12-12','2015-12-18',761),(1028,'2015-02-21','2015-03-06',964),(1030,'2015-02-12','2015-02-25',446),(1030,'2015-02-26','2015-03-04',560),(1031,'2015-01-24','2015-02-05',458),(1031,'2015-05-20','2015-05-25',873),(1031,'2015-10-27','2015-11-09',390),(1032,'2015-08-19','2015-08-30',240),(1033,'2015-04-22','2015-05-04',420),(1033,'2015-04-30','2015-05-09',769),(1033,'2016-03-28','2016-04-11',974),(1036,'2015-06-15','2015-06-24',420),(1037,'2015-04-18','2015-04-26',277),(1037,'2015-09-16','2015-09-27',959),(1038,'2015-01-13','2015-01-27',560),(1038,'2015-02-27','2015-03-10',854),(1038,'2015-08-08','2015-08-14',973),(1039,'2015-12-02','2015-12-16',647),(1040,'2015-04-05','2015-04-17',560),(1040,'2015-06-10','2015-06-16',874),(1040,'2015-11-25','2015-12-03',277),(1041,'2015-05-23','2015-06-02',873),(1042,'2015-12-01','2015-12-09',769),(1043,'2015-04-01','2015-04-14',870),(1043,'2015-08-12','2015-08-21',247),(1044,'2015-06-10','2015-06-17',232),(1044,'2015-08-24','2015-08-31',825),(1044,'2015-11-21','2015-12-03',458),(1045,'2015-03-15','2015-03-29',964),(1045,'2015-08-12','2015-08-25',490),(1045,'2015-09-07','2015-09-21',304),(1045,'2015-11-23','2015-12-05',288),(1045,'2015-12-09','2015-12-17',319),(1046,'2015-11-08','2015-11-14',987),(1047,'2015-01-31','2015-02-10',172),(1049,'2015-01-23','2015-02-04',304),(1049,'2015-02-07','2015-02-15',854),(1050,'2015-08-12','2015-08-22',647),(1050,'2015-12-17','2015-12-23',854),(1052,'2015-03-17','2015-03-28',987),(1053,'2015-05-25','2015-06-07',406),(1054,'2015-04-23','2015-05-02',973),(1055,'2015-05-15','2015-05-28',319),(1057,'2015-08-12','2015-08-25',446),(1058,'2015-02-13','2015-02-21',103),(1058,'2015-04-12','2015-04-21',406),(1058,'2015-07-27','2015-08-09',964),(1058,'2015-08-21','2015-08-27',516),(1058,'2015-09-28','2015-10-10',209),(1059,'2015-06-03','2015-06-15',247),(1060,'2015-05-16','2015-05-26',523),(1060,'2015-06-28','2015-07-10',560),(1062,'2015-10-16','2015-10-30',874),(1063,'2015-02-04','2015-02-14',490),(1063,'2015-06-12','2015-06-17',854),(1064,'2015-08-10','2015-08-15',170),(1064,'2015-09-14','2015-09-21',272),(1065,'2015-05-05','2015-05-16',103),(1065,'2015-12-14','2015-12-26',870),(1066,'2015-03-24','2015-04-05',406),(1067,'2015-02-09','2015-02-18',272),(1068,'2015-12-26','2016-01-04',631),(1069,'2015-05-17','2015-05-22',232),(1071,'2015-03-04','2015-03-09',959),(1071,'2015-10-23','2015-11-02',738),(1071,'2015-12-16','2015-12-26',962),(1072,'2015-04-04','2015-04-13',523),(1074,'2015-01-28','2015-02-08',490),(1074,'2015-08-26','2015-09-05',406),(1075,'2015-09-29','2015-10-08',552),(1076,'2015-01-13','2015-01-25',523),(1076,'2015-12-12','2015-12-23',103),(1078,'2015-03-12','2015-03-19',277),(1078,'2015-07-13','2015-07-27',964),(1079,'2015-07-24','2015-07-30',825),(1080,'2015-01-20','2015-01-30',631),(1080,'2015-07-15','2015-07-22',962),(1081,'2015-05-01','2015-05-09',406),(1081,'2015-08-15','2015-08-20',738),(1081,'2016-03-28','2016-04-11',974),(1082,'2015-07-20','2015-07-26',523),(1083,'2015-09-10','2015-09-23',420),(1083,'2015-10-23','2015-11-02',924),(1083,'2015-11-01','2015-11-09',209),(1083,'2015-12-23','2016-01-01',870),(1084,'2015-06-05','2015-06-10',103),(1085,'2015-08-16','2015-08-22',870),(1087,'2015-05-11','2015-05-18',304),(1088,'2015-03-25','2015-04-08',170),(1088,'2015-09-17','2015-09-27',560),(1088,'2015-09-30','2015-10-11',390),(1090,'2015-08-01','2015-08-06',769),(1090,'2015-09-28','2015-10-08',420),(1091,'2015-06-08','2015-06-18',987),(1093,'2015-02-17','2015-03-03',516),(1093,'2015-07-28','2015-08-10',240),(1093,'2015-10-12','2015-10-26',446),(1094,'2015-05-20','2015-05-25',172),(1094,'2015-09-24','2015-10-03',287),(1094,'2015-09-30','2015-10-05',873),(1095,'2015-02-12','2015-02-17',987),(1096,'2015-03-18','2015-03-30',729),(1096,'2015-04-19','2015-05-02',406),(1101,'2015-09-11','2015-09-25',277),(1102,'2015-05-03','2015-05-16',232),(1103,'2015-01-13','2015-01-20',304),(1103,'2015-01-14','2015-01-23',288),(1103,'2015-05-14','2015-05-27',924),(1104,'2015-06-12','2015-06-24',873),(1104,'2015-06-26','2015-07-04',103),(1104,'2015-08-09','2015-08-17',170),(1105,'2015-04-01','2015-04-12',761),(1106,'2015-03-05','2015-03-16',874),(1106,'2015-12-01','2015-12-08',420),(1108,'2015-06-26','2015-07-05',277),(1109,'2015-05-25','2015-05-30',873),(1109,'2015-07-05','2015-07-19',894),(1110,'2015-01-16','2015-01-25',987),(1110,'2015-12-14','2015-12-25',825),(1111,'2015-05-07','2015-05-20',894),(1112,'2015-01-25','2015-02-03',406),(1112,'2015-06-24','2015-07-07',692),(1113,'2015-02-07','2015-02-16',304),(1113,'2015-07-06','2015-07-16',552),(1114,'2015-06-17','2015-06-28',870),(1115,'2015-04-25','2015-05-01',647),(1115,'2015-05-03','2015-05-16',589),(1115,'2015-09-04','2015-09-09',959),(1115,'2015-10-01','2015-10-06',783),(1115,'2015-10-18','2015-10-31',288),(1115,'2015-11-19','2015-11-24',924),(1116,'2015-09-07','2015-09-20',319),(1117,'2015-09-20','2015-09-26',278),(1118,'2015-10-30','2015-11-08',458),(1118,'2015-11-04','2015-11-13',825),(1119,'2015-12-19','2016-01-02',446),(1119,'2015-12-20','2015-12-29',277),(1120,'2015-02-10','2015-02-23',516),(1121,'2015-07-16','2015-07-24',287),(1121,'2015-08-03','2015-08-14',390),(1121,'2015-12-20','2015-12-31',825),(1125,'2015-01-01','2015-01-11',692),(1125,'2015-09-14','2015-09-21',874),(1126,'2015-01-14','2015-01-20',959),(1126,'2015-05-18','2015-05-28',924),(1126,'2015-08-11','2015-08-16',915),(1128,'2015-05-14','2015-05-27',240),(1128,'2015-09-27','2015-10-04',769),(1128,'2015-10-04','2015-10-09',873),(1129,'2015-08-06','2015-08-18',589),(1130,'2015-03-13','2015-03-19',523),(1130,'2015-12-14','2015-12-21',458),(1132,'2015-11-19','2015-11-29',962),(1133,'2015-05-05','2015-05-16',964),(1133,'2015-12-06','2015-12-14',277),(1134,'2015-01-30','2015-02-13',232),(1135,'2015-07-19','2015-07-28',446),(1135,'2015-09-06','2015-09-14',211),(1136,'2015-02-20','2015-03-02',825),(1136,'2015-05-19','2015-06-02',870),(1140,'2015-02-15','2015-02-25',761),(1141,'2015-01-12','2015-01-21',446),(1143,'2016-03-28','2016-04-11',974);
/*!40000 ALTER TABLE `bookloan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrower`
--

DROP TABLE IF EXISTS `borrower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `borrower` (
  `borrowerNo` int(4) NOT NULL AUTO_INCREMENT,
  `borrowerName` varchar(255) NOT NULL,
  `borrowerAddress` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`borrowerNo`),
  UNIQUE KEY `borrowerName` (`borrowerName`)
) ENGINE=InnoDB AUTO_INCREMENT=976 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrower`
--

LOCK TABLES `borrower` WRITE;
/*!40000 ALTER TABLE `borrower` DISABLE KEYS */;
INSERT INTO `borrower` VALUES (172,'Willy Corker','5048 Emerald Village, Two Chestnut, Maryland, 21507-0313, US, (301) 542-0241\"\r\n406,\"Earl Valliere'),(209,'Hildegard Philipps','9817 Grand Centre, Cardtown, South Carolina, 29245-6230, US, (843) 252-1339\"\r\n783,\"Paulita Scott'),(211,'Shanna Korte','3231 Round Cape, Alabama Village, Vermont, 05551-3544, US, (802) 662-8007\"\r\n915,\"Charline Muse'),(240,'Raven Kemmer','7349 Velvet River Ridge, Soapstick, Ohio, 45854-7315, US, (234) 563-4435\"\r\n924,\"Antonetta Lenoir'),(277,'Rosalva Stelling','1011 Blue Autumn Limits, Troublesome, Quebec, G0W-3L6, CA, (418) 757-1698\"\r\n247,\"Glen Divers'),(304,'Shari Moultrie','7176 Heather Beacon Plaza, Latexo, New Brunswick, E2I-1V3, CA, (506) 592-6366\"\r\n516,\"Annamaria Bunde'),(319,'Doris Rothschild','1636 Hazy Farms, Shiney Town, New Mexico, 88315-8453, US, (575) 713-7977\"\r\n761,\"Dorthy Dean'),(390,'Roseann Wynne','1246 Tawny Vista, Badnation, Utah, 84657-6015, US, (385) 421-9537\"\r\n287,\"Kimberely Pilla'),(441,'Modesta Pou','3700 Crystal Oak Bend, Alta, California, 93629-6234, US, (714) 917-0274\"\r\n655,\"Jamee Mcmackin'),(458,'Albertina Zeiger','3561 Hidden Autoroute, Cathlapotle, North Dakota, 58167-2354, US, (701) 689-8833\"\r\n987,\"Eliseo Karls'),(490,'Stuart Amoroso','18 Thunder Log By-pass, Drip Rock, Manitoba, R6L-5H8, CA, (204) 548-5367\"\r\n959,\"Yer Futch'),(523,'Lean Durrance','3484 Fallen Freeway, Greasy Corner, New Brunswick, E0S-1K8, CA, (506) 922-6500\"\r\n420,\"Joan Kitchell'),(552,'Adam Rogge','2742 Burning Passage, Michigan Bar, Rhode Island, 02834-3860, US, (401) 340-7958\"\r\n278,\"Karey Caston'),(589,'Gino Bottorff','7450 Sleepy Island, Lingerlost, Maine, 04797-2429, US, (207) 531-8862\"\r\n854,\"Lucius Leonard'),(647,'Marybeth Sebesta','9852 Clear Avenue, Ah-Gwah-Ching, Virginia, 22229-9805, US, (276) 122-9154\"\r\n446,\"Octavio Lynn'),(692,'Arianne Setzer','236 Harvest Sky Diversion, Kremlin, Ontario, L7A-1J8, CA, (248) 256-3744\"\r\n738,\"Alex Pixler'),(713,'Madison Sherrer','4030 Dusty Goose Route, Buttzville, Oregon, 97936-0862, US, (541) 101-0554\"\r\n103,\"Afton Schweigert'),(729,'Emmie Belmont','1707 Merry Parade, Sizerock, Newfoundland, A1G-0H2, CA, (709) 873-5528\"\r\n170,\"Muoi Aguila'),(825,'Shemeka Nodine','7169 Stony Manor, Unfried, New Jersey, 07486-4521, US, (551) 341-8426\"\r\n631,\"Evangelina Harps'),(870,'Helaine Ingram','6832 Easy Nectar Pike, Nasketucket, Nunavut, X2Q-7Y4, CA, (867) 841-3728\"\r\n560,\"Sherryl Coppola'),(874,'Althea Sandage','3486 Cotton Lake Estates, Holy Cross, Wyoming, 82025-6668, US, (307) 291-3388\"\r\n873,\"Leoma Gillett'),(894,'Rosana Uphoff','8035 High Inlet, Gays Mills, Oklahoma, 73154-9329, US, (405) 080-9468\"\r\n288,\"Claris Venzon'),(962,'Tod Kerby','5685 Rustic Towers, Charity, Alberta, T8Z-1G8, CA, (780) 646-9363\"\r\n232,\"Tenisha Chiodo'),(964,'Hal Futrell','955 Red Nook, Dodge Hollow, Colorado, 81620-2557, US, (720) 916-0285\"\r\n769,\"Ina Burrill'),(973,'Lyndsey Bloch','1184 Golden Heath, Stargo, Michigan, 49469-4402, US, (906) 641-1870\"\r\n272,\"Brandon Cosme'),(974,'Test Man','123 rue Test');
/*!40000 ALTER TABLE `borrower` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-28 12:10:56
