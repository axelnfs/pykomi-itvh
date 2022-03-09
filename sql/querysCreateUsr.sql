CREATE USER admin IDENTIFIED BY '1234';

/*garantizar todos los privilegios de admin*/
GRANT ALL PRIVILEGES ON * . * TO 'admin';

/*para consultas desde lenguaje backend*/
CREATE USER userCommon IDENTIFIED BY '1234';

GRANT SELECT, SELECT ON * . * TO 'userCommon';
GRANT INSERT, SELECT ON * . * TO 'userCommon';
GRANT UPDATE, SELECT ON * . * TO 'userCommon';
GRANT DELETE, SELECT ON * . * TO 'userCommon';

