DROP TABLE IF EXISTS `mock_config`;
CREATE TABLE if not exists `mock_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `reqparams` varchar(500) DEFAULT NULL,
  `methods` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `resparams` varchar(500) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ischeck` int(1) DEFAULT NULL,
  `project_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;