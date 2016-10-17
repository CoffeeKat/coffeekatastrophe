DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_createPost(
    IN p_title CHAR(255),
    IN p_postdata TEXT,
    IN p_author_id BIGINT
)
BEGIN
      insert into blogposts
      (
          title,
          postdata,
          author_id
      )
      values
      (
          p_title,
          p_postdata,
          p_author_id
      );
END$$
DELIMITER ;
