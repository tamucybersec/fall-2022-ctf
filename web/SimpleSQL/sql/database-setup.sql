USE users;

CREATE TABLE users (
    username TEXT(20),
    password TEXT(32),
    phone TEXT(10),
    email TEXT(50),
    id TEXT(5)
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'admin',
    '6dd959dc01b4f641117fc14e5d7cec1f',
    '6904206969',
    'lmao@root.dev',
    '46290'
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'nhwn',
    '5a09a68ae092bea5376f6493b92d4467',
    '6969694200',
    'funnies@dia_nsa_dod.mil.gov.org.edu',
    '66600'
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'MITRE_man',
    '7d814b688b4cec0b02a1f68b2e078ac4',
    '9799776656',
    'hard@ware.man',
    '24000'
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'boba',
    '0033430fa4d6685518e0413572dc8b40',
    '9793304078',
    'boba_addict@lmao.com',
    '12350'
);

INSERT INTO users (username, password, phone, email, id) VALUES (
    'ret2rev',
    'b67de2b2bd406f88a82c1b49d71b6106',
    '555ret2rev',
    'ret2rev@uwu.edu',
    '06901'
);

CREATE TABLE flag (
    flag TEXT(128)
);

INSERT INTO flag (flag) VALUES (
    'gigem{th1s_1s_0nly_th3_b3g1nn1ng}'
);

REVOKE ALL ON *.* FROM 'ro_user'@'%';
GRANT SELECT ON *.* TO 'ro_user'@'%';
FLUSH PRIVILEGES;

