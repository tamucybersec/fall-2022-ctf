USE users;

CREATE TABLE users (
    username TEXT(50),
    password TEXT(50),
    phone TEXT(50),
    email TEXT(50),
    id TEXT(50)
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'admin',
    'gigem{not_the_real_flag_lmao}',
    '123-456-7890',
    'TacEx@root.lmao',
    '001'
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'nwhn',
    'https://tx.ag/pwnsimps',
    '420-420-lmao',
    'pwnsimp@lmao.dev',
    '002'
);

REVOKE ALL ON *.* FROM 'ro_user'@'%';
GRANT SELECT ON *.* TO 'ro_user'@'%';
GRANT FILE ON *.* TO 'ro_user'@'%';
FLUSH PRIVILEGES;

