/*
SQLyog Community v13.1.9 (64 bit)
MySQL - 10.4.25-MariaDB : Database - gym management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gym management` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `gym management`;

/*Table structure for table `allocation` */

DROP TABLE IF EXISTS `allocation`;

CREATE TABLE `allocation` (
  `alloc_id` int(11) NOT NULL AUTO_INCREMENT,
  `t_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`alloc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `allocation` */

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `attendance` varchar(10) NOT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `attendance` */

insert  into `attendance`(`a_id`,`u_id`,`t_id`,`date`,`attendance`) values 
(1,9,19,'2022-10-29','present'),
(2,18,19,'2022-10-29','present'),
(3,7,23,'2022-10-30','present'),
(4,7,23,'2022-10-30','present'),
(5,37,23,'2022-10-31','present'),
(6,40,23,'2022-10-31','present'),
(7,54,23,'2022-11-19','present'),
(8,54,23,'2022-11-20','absent'),
(9,54,23,'2022-11-21','present'),
(10,54,23,'2022-11-22','present');

/*Table structure for table `bodymeasurement` */

DROP TABLE IF EXISTS `bodymeasurement`;

CREATE TABLE `bodymeasurement` (
  `bd_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `shoulder` varchar(40) NOT NULL,
  `right_shoulder_to_elbow` varchar(40) NOT NULL,
  `right_elbow_to_hand` varchar(40) NOT NULL,
  `left_shoulder_to_elbow` varchar(40) NOT NULL,
  `left_elbow_to_hand` varchar(40) NOT NULL,
  `right_waist_to_knee` varchar(40) NOT NULL,
  `right_knee_to_foot` varchar(40) NOT NULL,
  `left_waist_to_knee` varchar(40) NOT NULL,
  `left_knee_to_foot` varchar(40) NOT NULL,
  PRIMARY KEY (`bd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `bodymeasurement` */

insert  into `bodymeasurement`(`bd_id`,`u_id`,`date`,`shoulder`,`right_shoulder_to_elbow`,`right_elbow_to_hand`,`left_shoulder_to_elbow`,`left_elbow_to_hand`,`right_waist_to_knee`,`right_knee_to_foot`,`left_waist_to_knee`,`left_knee_to_foot`) values 
(1,7,'2022-10-17','34','56','77','86','56','45','76','54','43'),
(2,18,'2022-10-28','43','34','65','65','65','65','65','65','65'),
(4,40,'2022-10-31','43','65','65','65','65','65','65','65','65'),
(5,54,'2022-11-18','54','54','54','54','65','76','65','54','54'),
(6,54,'2022-11-19','34','65','65','66','56','65','76','76','76'),
(7,54,'2022-11-22','65','67','76','87','65','56','45','65','76'),
(8,54,'2022-11-22','57','58','57','59','59','69','60','67','67');

/*Table structure for table `diet plan` */

DROP TABLE IF EXISTS `diet plan`;

CREATE TABLE `diet plan` (
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  `dietname` varchar(20) NOT NULL,
  `t_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

/*Data for the table `diet plan` */

insert  into `diet plan`(`d_id`,`dietname`,`t_id`,`u_id`,`description`) values 
(1,'efjhef',17,9,'efioueyf'),
(4,'add',17,7,'up'),
(7,'weight gain',19,7,'nuitrient food must eat'),
(8,'weight gain',23,40,'MUST EAT MEALS DAILY'),
(13,'weight gain',23,54,'must  eat meals daily '),
(14,'CARDIO ',23,57,'FOR WEIGHT LOSS.DAILY WORKOUT IMPORTANT');

/*Table structure for table `equipments` */

DROP TABLE IF EXISTS `equipments`;

CREATE TABLE `equipments` (
  `e_id` int(11) NOT NULL AUTO_INCREMENT,
  `e_name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  `image` varchar(300) NOT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `equipments` */

insert  into `equipments`(`e_id`,`e_name`,`description`,`image`) values 
(5,'DUMBELL','must workout 20 times','hero-bg_.jpg'),
(6,'PULL UP BAR','It is used to pull up','cardiac.jpg');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`f_id`,`u_id`,`feedback`,`date`) values 
(3,40,'GOOD GYM','2022-10-30'),
(5,54,'feedback','2022-11-19'),
(6,57,'nice gym','2022-11-29');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `user type` varchar(10) NOT NULL,
  PRIMARY KEY (`l_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`l_id`,`u_name`,`password`,`user type`) values 
(1,'admin','admin','admin'),
(2,'user','user','user'),
(3,'trainer','trainer','personal'),
(4,'aswin','Aswin0000','user'),
(5,'anand','anand','trainer'),
(6,'Rajuraju','Raju0087','user'),
(7,'junaid','Junaid123','user'),
(8,'yedu@0089','yedu0089','trainer'),
(9,'Alan','Alan00890089','user'),
(10,'rahul','Rahul0089','trainer'),
(11,'midhun','Midhun799','user'),
(12,'shamna','Shamna123','trainer'),
(13,'scissna','Scissna123','trainer'),
(14,'rahulrahul','Rahul123123','trainer'),
(15,'jithukrishnan','Jithukrishnan90','trainer'),
(16,'alanalan','Alanalan0','user'),
(17,'trainer','Trainer00','trainer'),
(18,'sanan','Sananpv90','user'),
(20,'hasna','Hasnabacker0','user'),
(21,'hasna','Hasnabacker0','user'),
(22,'aiswarya','Aiswarya123','trainer'),
(23,'jithu','Jithu123','trainer'),
(24,'asd','Asd123@1234','trainer'),
(25,'asd','Asd123@1234','trainer'),
(26,'asd','Asd123@1234','trainer'),
(27,'asd','Asd123@1234','trainer'),
(28,'asd','Asd123@1234','trainer'),
(29,'midhun','Midhun123','trainer'),
(30,'jathav','Jathav123','trainer'),
(31,'jishnu','Jishnu987','trainer'),
(32,'jishnu','Jishnu987','trainer'),
(33,'aiswarya','Aisw2rya888','trainer'),
(34,'jishnu','Aisw@rya123','trainer'),
(35,'aiswarya','Aiswarya123','trainer'),
(36,'aswin','Aswin2123','trainer'),
(37,'MIDHUN','Midhun123','user'),
(38,'junaid','Junaid123','user'),
(39,'sanan','Sanan123','user'),
(40,'anand','Anand123','user'),
(41,'abin','Abin1234','user'),
(42,'anees','Anees123','user'),
(43,'ajmal','Ajmal123','trainer'),
(44,'sharon','Sharon123','user'),
(45,'scissna','Scissna123','user'),
(46,'aswin','Aswin123','user'),
(47,'sharon','Sharon123','user'),
(48,'dtfyguhij','hallaHalla5','user'),
(49,'sharon','Sharon123','user'),
(50,'sharonjhj','Sharon123','user'),
(51,'sharon','Sharon123','user'),
(52,'sharon','Sharon123','user'),
(53,'ajith','Ajith123','trainer'),
(54,'shadow','Shadow123','user'),
(55,'midhun','Midhun123','user'),
(56,'alen','Alen@123','user'),
(57,'kuttan','Kuttan@123','user');

/*Table structure for table `membership` */

DROP TABLE IF EXISTS `membership`;

CREATE TABLE `membership` (
  `m_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `payment_status` varchar(40) NOT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `membership` */

insert  into `membership`(`m_id`,`u_id`,`date`,`payment_status`) values 
(6,40,'2022-10-30','1000'),
(7,54,'2022-11-17','1000'),
(8,18,'2022-11-22','1000'),
(9,7,'2022-11-22','1000'),
(10,56,'2022-11-22','1000'),
(11,57,'2022-11-22','1000');

/*Table structure for table `package` */

DROP TABLE IF EXISTS `package`;

CREATE TABLE `package` (
  `pack_id` int(11) NOT NULL AUTO_INCREMENT,
  `p_name` varchar(20) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`pack_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `package` */

insert  into `package`(`pack_id`,`p_name`,`price`,`description`) values 
(4,'WEIGHT LOSS',2000,'An overweight is always at higher risk of developing serious health problem'),
(5,'WEIGHT GAIN',2500,'The package is for everyone who want to gain weight in natural and healthy weight'),
(6,'CARDIO VASCULAR TRAI',2600,'Increase your amount of cardio while weight lifting to increase carolic ');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `pk_id` int(11) DEFAULT NULL,
  `amount` varchar(400) NOT NULL,
  `date` varchar(400) NOT NULL,
  `screen_shot` text NOT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`u_id`,`pk_id`,`amount`,`date`,`screen_shot`) values 
(1,54,5,'2500','2022-11-21','QR.jpg'),
(2,18,5,'2500','2022-11-22','QR.jpg'),
(3,7,6,'2600','2022-11-22','QR.jpg'),
(4,57,5,'2500','2022-11-22','QR.jpg');

/*Table structure for table `registration` */

DROP TABLE IF EXISTS `registration`;

CREATE TABLE `registration` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `gender` varchar(5) DEFAULT NULL,
  `dob` varchar(10) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `ph_no` bigint(20) DEFAULT NULL,
  `height` varchar(11) NOT NULL,
  `weight` varchar(11) NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

/*Data for the table `registration` */

insert  into `registration`(`u_id`,`l_id`,`username`,`place`,`gender`,`dob`,`email`,`ph_no`,`height`,`weight`) values 
(4,40,'ANAND','MAAHI','male','2004-12-10','anand123@gmail.com',7634857634,'167','56'),
(16,54,'shadow','palace','male','2004-12-18','shadow@gamil.com',8777878789,'158','66'),
(17,55,'MIDHUN','koduvally','male','2004-12-25','midhun@gmail.com',9887766564,'141','65'),
(18,56,'Alen','manathavady','male','2004-12-22','alen12@gmail.com',8786786786,'156','56'),
(19,57,'kuttan','koduvally','male','2004-12-12','kuttan12@gmail.com',8759875645,'176','76');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `r_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  `request` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`r_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `request` */

insert  into `request`(`r_id`,`u_id`,`t_id`,`request`,`status`,`date`) values 
(1,54,1,' I need a personal trainer','assigned','2022-11-22');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `re_id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(100) NOT NULL,
  `u_id` int(11) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`re_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `review` */

/*Table structure for table `schedule personal user` */

DROP TABLE IF EXISTS `schedule personal user`;

CREATE TABLE `schedule personal user` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `from_time` time NOT NULL,
  `to_time` time NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `schedule personal user` */

insert  into `schedule personal user`(`s_id`,`u_id`,`t_id`,`date`,`from_time`,`to_time`) values 
(1,54,23,'2022-11-17','20:46:00','18:46:00'),
(2,54,23,'2022-11-22','07:50:00','09:50:00');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_name` varchar(20) NOT NULL,
  `image` text NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `service` */

insert  into `service`(`s_id`,`s_name`,`image`,`description`) values 
(1,'cardiac training','cardiac.jpg','In addition to keeping your heart and lungs in shape, CV training burns calories and is your primary'),
(2,'PERSONAL TRAINER','PERSONAL.jpg','Personal trainers are responsible for educating clients and enforcing policies regarding safe and pr'),
(3,'Zumba dance','zumba.jpg','Zumba is an interval workout. The classes move between high- and low-intensity dance moves designed ');

/*Table structure for table `trainer` */

DROP TABLE IF EXISTS `trainer`;

CREATE TABLE `trainer` (
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `ph_no` bigint(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `type` varchar(20) NOT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`t_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `ph_no` (`ph_no`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `trainer` */

insert  into `trainer`(`t_id`,`l_id`,`name`,`place`,`gender`,`ph_no`,`email`,`dob`,`type`,`qualification`) values 
(1,23,'jithu','wayanad','male',2147483647,'jithu@gmail.com','2019-12-12','Personal trainer','12 th'),
(14,36,'aswin','krishna','male',9878654567,'anu@gmail.com','2002-01-03','Personal trainer','10 th'),
(15,43,'ajmal','valad','male',7676767676,'ajmal123@gmail.com','2019-12-18','General trainer','12 th'),
(16,53,'AJITH','ALATTIL','male',9608970922,'ajithjhonson@gamil.c','2004-12-08','Personal trainer','AMHSSC');

/*Table structure for table `work_hourper` */

DROP TABLE IF EXISTS `work_hourper`;

CREATE TABLE `work_hourper` (
  `wrk_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `date` varchar(40) NOT NULL,
  `from_time` varchar(40) NOT NULL,
  `to_time` varchar(40) NOT NULL,
  PRIMARY KEY (`wrk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `work_hourper` */

/*Table structure for table `workout hour` */

DROP TABLE IF EXISTS `workout hour`;

CREATE TABLE `workout hour` (
  `pwrk_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_time` varchar(30) NOT NULL,
  `to_time` varchar(30) NOT NULL,
  `day` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  PRIMARY KEY (`pwrk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `workout hour` */

/*Table structure for table `workout_user` */

DROP TABLE IF EXISTS `workout_user`;

CREATE TABLE `workout_user` (
  `wrk_id` int(11) NOT NULL AUTO_INCREMENT,
  `t_id` int(11) NOT NULL,
  `workout` varchar(100) NOT NULL,
  `tip` varchar(100) NOT NULL,
  PRIMARY KEY (`wrk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `workout_user` */

insert  into `workout_user`(`wrk_id`,`t_id`,`workout`,`tip`) values 
(1,23,'push up','20 Push up every morning and evening'),
(2,23,'pull up','must do 60 pull up daily '),
(3,23,'sit up','must do 50 situp');

/*Table structure for table `wrk_gen` */

DROP TABLE IF EXISTS `wrk_gen`;

CREATE TABLE `wrk_gen` (
  `wrk_hid` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(12) NOT NULL,
  `from_time` varchar(11) NOT NULL,
  `to_time` varchar(11) NOT NULL,
  PRIMARY KEY (`wrk_hid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `wrk_gen` */

insert  into `wrk_gen`(`wrk_hid`,`day`,`from_time`,`to_time`) values 
(2,'TUESDAY','5AM','9PM'),
(3,'WEDNESDAY','5AM','9PM'),
(4,'THURSDAY','5AM','9PM'),
(5,'FRIDAY','5AM','9PM'),
(6,'SATURDAY','9AM','8PM'),
(7,'MONDAY','6AM','9PM');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
