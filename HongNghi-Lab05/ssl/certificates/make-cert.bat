openssl req -new -x509 -newkey rsa:2048 -nodes -keyout server-key.key -out server-cert.crt -days 365 -config ssl\certificates\server-cert.cnf
