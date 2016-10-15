DELIMITER $$
CREATE DEFINER=root@localhost PROCEDURE sp_createUser(
    IN p_name CHAR(255),
    IN p_username CHAR(255),
    IN p_email VARCHAR(320),
    IN p_password CHAR(255)
)
BEGIN
    if ( select exists (select 1 from users where username = p_username) ) THEN

        select 'Username Exists';

    ELSE
        insert into users
        (
            name,
            username,
            email,
            password
        )
        values
        (
            p_name,
            p_username,
            p_email,
            p_password
        );

    END IF;
END$$
DELIMITER ;
