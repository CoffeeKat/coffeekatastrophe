DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_getposts(
    IN p_tag CHAR(255),
    IN p_offset INT,
    IN p_qty INT
)
BEGIN
    SELECT blogposts.* FROM
    (blogposts INNER JOIN tagpostrelation ON
    tagpostrelation.post_id = blogposts.id)
    INNER JOIN posttags ON
    posttags.id = tagpostrelation.tag_id
    WHERE posttags.tag = p_tag
    LIMIT p_offset, p_qty;

END$$
DELIMITER ;
