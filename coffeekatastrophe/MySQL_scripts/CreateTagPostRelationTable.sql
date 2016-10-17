CREATE TABLE tagpostrelation (
id BIGINT NOT NULL AUTO_INCREMENT,
tag_id BIGINT NOT NULL,
post_id BIGINT NOT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`tag_id`) REFERENCES posttags(id),
FOREIGN KEY (`post_id`) REFERENCES blogposts(id)
);
