DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_validateLogin(
IN p_username CHAR(255)
)
BEGIN
    select * from users where username = p_username;
END$$
DELIMITER ;
