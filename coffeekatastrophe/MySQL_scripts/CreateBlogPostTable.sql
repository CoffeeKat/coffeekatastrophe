CREATE TABLE blogposts (
id BIGINT NOT NULL AUTO_INCREMENT,
title CHAR(255) NOT NULL,
postdata TEXT NOT NULL,
author_id BIGINT NOT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`author_id`) REFERENCES users(id)
);
