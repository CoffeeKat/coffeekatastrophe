DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_gettagid(
IN p_tag CHAR(255)
)
BEGIN
    select * from posttags where tag = p_tag;
END$$
DELIMITER ;
