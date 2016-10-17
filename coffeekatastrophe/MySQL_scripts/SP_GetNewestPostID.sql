DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_getnewestpostid()
BEGIN
    select max(id) from blogposts;
END$$
DELIMITER ;
