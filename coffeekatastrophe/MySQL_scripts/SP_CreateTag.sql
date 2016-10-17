DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_createTag(
    IN p_tag CHAR(255)
)
BEGIN
    IF NOT ( select exists (select 1 from posttags where tag = p_tag) ) THEN
      insert into posttags
      (
          tag
      )
      values
      (
          p_tag
      );
    END IF;
END$$
DELIMITER ;
