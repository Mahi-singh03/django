# Meta Back End Developer Capstone

## Quick Setup (Without mysql database)
1. git clone this repository
2. Run `pipenv install` in the terminal
3. Run `pipenv shell` in the terminal
4. Run `cd littlelemon`
5. Run `python manage.py runserver`

## Database (mysql) Setup
1. You need to install your mysql server
2. Make sure start the server
3. Login into mysqlclient using `mysql -u root -p <the password you set when installing mysql server>`
4. In mysql, run the following commands
   1. `CREATE DATABASE LittleLemon;`
   2. `CREATE USER 'littlelemonadmin'@'localhost' IDENTIFIED BY 'littlelemon';`
   3. `GRANT ALL LittleLemon.* TO 'littlelemonadmin'@'localhost';`
   4. `FLUSH PRIVILEGES;`
   5. `GRANT ALL test_littlelemon.* TO 'littlelemonadmin'@'localhost';`
   6. `FLUSH PRIVILEGES;`