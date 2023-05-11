/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 50741
 Source Host           : localhost:3306
 Source Schema         : tank

 Target Server Type    : MySQL
 Target Server Version : 50741
 File Encoding         : 65001

 Date: 11/05/2023 21:36:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_1_defeat` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_2_defeat` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of history
-- ----------------------------
INSERT INTO `history` VALUES (1, '张三', '2023-04-20 20:29:54.481594', '单人', '11', '0');
INSERT INTO `history` VALUES (2, '张三', '2023-04-20 20:30:29.621320', '双人', '0', '0');
INSERT INTO `history` VALUES (3, '张三', '2023-04-20 20:31:36.850316', '单人', '0', '0');
INSERT INTO `history` VALUES (4, '张三', '2023-05-04 13:41:58.447278', '双人', '0', '0');
INSERT INTO `history` VALUES (5, '张三', '2023-05-04 14:17:50.895560', '双人', '0', '0');
INSERT INTO `history` VALUES (6, '张三', '2023-05-04 21:19:39.875315', '单人', '1', '0');
INSERT INTO `history` VALUES (7, '张三', '2023-05-05 08:18:20.491221', '单人', '0', '0');
INSERT INTO `history` VALUES (8, '张三', '2023-05-05 08:19:25.455180', '双人', '2', '0');
INSERT INTO `history` VALUES (9, '张三', '2023-05-11 21:11:12.716446', '单人', '8', '0');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, '张三', '123456');

SET FOREIGN_KEY_CHECKS = 1;
