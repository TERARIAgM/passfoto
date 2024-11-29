USE mysql;
UPDATE user SET authentication_string=PASSWORD('Romazamzama12') WHERE user='root';
FLUSH PRIVILEGES;
EXIT;
