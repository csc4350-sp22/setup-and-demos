# If any of the below don't work, you can try
- adding "sudo" in front of the command
- switching "pip" for "pip3"

# WSL

## GitHub
```
ssh-keygen  # then hit Enter until all the prompts are done
cat ~/.ssh/id_rsa.pub  # Copy the output of this command where GitHub asks you for an SSH key
```
## Python
```
sudo apt-get update  # update your installer so the Pip installation works
sudo apt install python3-pip  # install pip, which manages python packages
pip3 install flask
pip3 install requests
pip3 install python-dotenv
```

## Heroku
`sudo curl https://cli-assets.heroku.com/install.sh | sh   # install Heroku`

Create a free account on Heroku: https://signup.heroku.com/login

## PostgreSQL setup
```
sudo apt install postgresql
sudo -u postgres psql  # just testing that psql is installed. You should get an interactive prompt. Quit by entering "\q"
pip3 install psycopg2-binary
pip3 install Flask-SQLAlchemy==2.1
```

# Mac

## GitHub
```
ssh-keygen  # then hit Enter until all the prompts are done
cat ~/.ssh/id_rsa.pub  # Copy the output of this command where GitHub asks you for an SSH key
```

## Python
```
python3 -m ensurepip --upgrade  # install pip, which manages python packages
pip3 install flask
pip3 install requests
pip3 install python-dotenv
```

## Heroku
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)  # install Homebrew
brew tap heroku/brew && brew install heroku  # install Heroku CLI
```

Create a free account on Heroku: https://signup.heroku.com/login

## PostgreSQL setup
```
brew install postgresql
brew services start postgresql
psql -h localhost  # this is just to test out that postgresql is installed okay - type "\q" to quit
# if the above command gives you an error like "database <user> does not exist," try the workaround in this link: https://stackoverflow.com/questions/17633422/psql-fatal-database-user-does-not-exist
pip3 install psycopg2-binary
pip3 install Flask-SQLAlchemy==2.1
```