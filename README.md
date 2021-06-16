# device_manage

使用方法
1. 建立数据库表
CREATE TABLE `tb_device`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serial` varchar(63) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `type` varchar(31) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `os` varchar(31) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `version` varchar(31) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `model` varchar(63) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `fitting` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `owner` varchar(31) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `user` varchar(31) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `since` datetime(0) DEFAULT NULL,
  `condition` int(31) DEFAULT NULL,
  `screen` varchar(31) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;


DROP TABLE IF EXISTS `tb_device_history`;
CREATE TABLE `tb_device_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `device_id` int(11) DEFAULT NULL,
  `to` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `from` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `date` datetime(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

2. 修改config.ini中 mysql配置

3. python main.py
