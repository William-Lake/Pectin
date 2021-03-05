BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `relationship_type` (
	`relationship_type_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`object_type_id_1`	INTEGER NOT NULL,
	`object_type_id_2`	INTEGER NOT NULL,
	`name`	TEXT NOT NULL,
	`description`	TEXT NOT NULL,
	FOREIGN KEY(`object_type_id_2`) REFERENCES `object_type`(`object_type_id`),
	FOREIGN KEY(`object_type_id_1`) REFERENCES `object_type`(`object_type_id`)
);
CREATE TABLE IF NOT EXISTS `relationship` (
	`relationship_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`relationship_type_id`	INTEGER NOT NULL,
	`object_id_1`	INTEGER NOT NULL,
	`object_id_2`	INTEGER NOT NULL,
	`name`	TEXT NOT NULL,
	FOREIGN KEY(`relationship_type_id`) REFERENCES `relationship_type`(`relationship_type_id`),
	FOREIGN KEY(`object_id_1`) REFERENCES `object`(`object_id`),
	FOREIGN KEY(`object_id_2`) REFERENCES `object`(`object_id`)
);
CREATE TABLE IF NOT EXISTS `question` (
	`question_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`content_id`	INTEGER NOT NULL,
	`target_table`	TEXT,
	`target_id`	INTEGER,
	`asked`	INTEGER NOT NULL DEFAULT 0 CHECK("asked" IN ( 0 , 1 )),
	`created`	timestamp NOT NULL DEFAULT current_timestamp,
	FOREIGN KEY(`content_id`) REFERENCES `content`(`content_id`)
);
CREATE TABLE IF NOT EXISTS `object_type` (
	`object_type_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT NOT NULL,
	`description`	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `object` (
	`object_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`object_type_id`	INTEGER NOT NULL,
	`name`	TEXT NOT NULL,
	FOREIGN KEY(`object_type_id`) REFERENCES `object_type`(`object_type_id`)
);
CREATE TABLE IF NOT EXISTS `content` (
	`content_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`text`	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `attribute_type` (
	`attribute_type_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT NOT NULL,
	`description`	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `attribute` (
	`attribute_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`attribute_type_id`	INTEGER NOT NULL,
	`name`	TEXT NOT NULL,
	FOREIGN KEY(`attribute_type_id`) REFERENCES `attribute_type`(`attribute_type_id`)
);
CREATE TABLE IF NOT EXISTS `answer_content` (
	`answer_content_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`answer_id`	INTEGER NOT NULL,
	`content_id`	INTEGER NOT NULL,
	FOREIGN KEY(`answer_id`) REFERENCES `answer`(`answer_id`),
	FOREIGN KEY(`content_id`) REFERENCES `content`(`content_id`)
);
CREATE TABLE IF NOT EXISTS `answer` (
	`answer_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`question_id`	INTEGER NOT NULL,
	FOREIGN KEY(`question_id`) REFERENCES `question`(`question_id`)
);
COMMIT;
