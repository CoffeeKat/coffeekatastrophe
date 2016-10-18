DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_createEditedPost(
    IN p_id BIGINT,
    IN p_title CHAR(255),
    IN p_postdata TEXT,
    IN p_author_id BIGINT
)
BEGIN
      UPDATE blogposts
      SET title = p_title, postdata = p_postdata, author_id = p_author_id
      WHERE id = p_id;
END$$
DELIMITER ;
