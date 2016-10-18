DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_getpostbyid(
    IN p_id BIGINT
)
BEGIN
    SELECT * FROM blogposts
    WHERE id = p_id;
END$$
DELIMITER ;
