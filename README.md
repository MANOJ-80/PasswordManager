# Password Manager


A secure password manager implemented in Python using MySQL, SHA256 for hashing the master password, Uses [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) for key hashing, and AES-256 for encryption/decryption.

## Features

- **Secure Storage**: All passwords are securely stored using AES encryption.
- **Master Password**: Uses a strong master password hashed with SHA256 for access.
- **Key Hashing**: Implements PBKDF2 for deriving encryption keys, enhancing security.
- **MySQL Database**: Password hashes are stored in a MySQL database.


# Installation

You need to have python3 to run this Project on Windows, Linux or MacOS

## Linux

### Clone this repository to your local machine
```
git clone https://github.com/MANOJ-80/PasswordManager.git
```

### Install Python Requirements
```
sudo apt install python3-pip
pip install -r requirements.txt
```
    
### Mysql
```
sudo apt install mysql-server
```
     
#### Create user 'PasswordManager' and grant permissions
**Login to mysql as root**  

```
sudo mysql -u root
```
**Create User**
```
CREATE USER 'PasswordManager'@localhost IDENTIFIED BY 'password';
```
**Grant privileges**
```
GRANT ALL PRIVILEGES ON *.* TO 'PasswordManager'@localhost IDENTIFIED BY 'password';
```
     
     
## Run
### Configure

You need to first configure the password manager by choosing a MASTER PASSWORD. This config step is only required to be executed once.
```
python config.py 
```
The above command will make a new configuration by asking you to choose a MASTER PASSWORD.
This will generate the DEVICE SECRET, create Database and required tables.


### Usage
```
python pm.py -h
usage: pm.py [-h] [-s NAME] [-u URL] [-e EMAIL] [-l LOGIN] [--length LENGTH] [-c] option

Description

positional arguments:
  option                (a)dd / (e)xtract / (g)enerate

optional arguments:
  -h, --help            show this help message and exit
  -s NAME, --name NAME  Site name
  -u URL, --url URL     Site URL
  -e EMAIL, --email EMAIL
                        Email
  -l LOGIN, --login LOGIN
                        Username
  --length LENGTH       Length of the password to generate
  -c, --copy            Copy password to clipboard
```


### Add entry
```
python pm.py add -s mysite -u mysite.com -e hello@email.com -l myusername
```
### Retrieve entry
```
python pm.py extract
```
The above command retrieves all the entries
```
python pm.py e -s mysite
```
The above command retrieves all the entries whose site name is "mysite"
```
python pm.py e -s mysite -l myusername
```
The above command retrieves the entry whose site name is "mysite" and username is "myusername"
```
python pm.py e -s mysite -l myusername --copy
```
The above command copies the password of the site "mysite" and username "myusername" into the clipboard
### Generate Password
```
python pm.py g --length 15
```
The above command generates a password of length 15 and copies to clipboard*****

     



