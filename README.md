## bezreality scraper
It is a Python package that collect data from [bezreality](bezreality.cz), then
parse the collected data and save them into database.

### Installation
a. MongoDB
You should visit the [installation page](https://docs.mongodb.com/manual/installation/)
and check the platform you are using.

For example, the installation of community edition on Ubuntu:
1. Import the public key and create list of files for MongoDB
```
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

2. Update local packages and install MongoDB packages:
```
sudo apt-get update
sudo apt-get install -y mongodb-org
```

3. Start MongoDB and check the status:
```
sudo systemctl start mongod
sudo systemctl status mongod
```

b. Clone the repository

c. Install requirements
-requirements.txt-
- in progress

### Usage
Run the script:
```bash
$ python bez_realitky.py "brno"
```
See to output message.

### Outputs
...
