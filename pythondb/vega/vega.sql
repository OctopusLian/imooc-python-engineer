/*
Navicat MariaDB Data Transfer

Source Server         : localhost_3306
Source Server Version : 100120
Source Host           : localhost:3306
Source Database       : vega

Target Server Type    : MariaDB
Target Server Version : 100120
File Encoding         : 65001

Date: 2018-11-27 19:35:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_news
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(40) NOT NULL,
  `editor_id` int(10) unsigned NOT NULL,
  `type_id` int(10) unsigned NOT NULL,
  `content_id` char(12) NOT NULL,
  `is_top` tinyint(3) unsigned NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` enum('草稿','待审批','已审批','隐藏') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `editor_id` (`editor_id`),
  KEY `type_id` (`type_id`),
  KEY `state` (`state`),
  KEY `create_time` (`create_time`),
  KEY `is_top` (`is_top`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO `t_news` VALUES ('1', '新闻标题1', '2', '1', '1', '1', '2018-11-22 18:55:56', '2018-11-22 18:55:56', '待审批');

-- ----------------------------
-- Table structure for t_role
-- ----------------------------
DROP TABLE IF EXISTS `t_role`;
CREATE TABLE `t_role` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role` (`role`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_role
-- ----------------------------
INSERT INTO `t_role` VALUES ('2', '新闻编辑');
INSERT INTO `t_role` VALUES ('1', '管理员');

-- ----------------------------
-- Table structure for t_type
-- ----------------------------
DROP TABLE IF EXISTS `t_type`;
CREATE TABLE `t_type` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_type
-- ----------------------------
INSERT INTO `t_type` VALUES ('2', '体育');
INSERT INTO `t_type` VALUES ('5', '历史');
INSERT INTO `t_type` VALUES ('4', '娱乐');
INSERT INTO `t_type` VALUES ('3', '科技');
INSERT INTO `t_type` VALUES ('1', '要闻');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(500) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `username_2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'admin', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'admin@163.com', '1');
INSERT INTO `t_user` VALUES ('2', 'scott', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'scott@163.com', '1');
INSERT INTO `t_user` VALUES ('3', 'test_1', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_1@163.com', '2');
INSERT INTO `t_user` VALUES ('4', 'test_2', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_2@163.com', '2');
INSERT INTO `t_user` VALUES ('5', 'test_3', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_3@163.com', '2');
INSERT INTO `t_user` VALUES ('6', 'test_4', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_4@163.com', '2');
INSERT INTO `t_user` VALUES ('7', 'test_5', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_5@163.com', '2');
INSERT INTO `t_user` VALUES ('8', 'test_6', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_6@163.com', '2');
INSERT INTO `t_user` VALUES ('9', 'test_7', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_7@163.com', '2');
INSERT INTO `t_user` VALUES ('10', 'test_8', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_8@163.com', '2');
INSERT INTO `t_user` VALUES ('11', 'test_9', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_9@163.com', '2');
INSERT INTO `t_user` VALUES ('12', 'test_10', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_10@163.com', '2');
INSERT INTO `t_user` VALUES ('13', 'test_11', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'test_11@163.com', '2');
