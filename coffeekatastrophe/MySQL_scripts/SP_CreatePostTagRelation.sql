DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_createPostTagRelation(
    IN p_tag_id BIGINT,
    IN p_post_id BIGINT
)
BEGIN
      insert into tagpostrelation
      (
          tag_id,
          post_id
      )
      values
      (
          p_tag_id,
          p_post_id
      );
END$$
DELIMITER ;
