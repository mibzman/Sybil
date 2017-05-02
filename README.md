# Sybil
A Natural Language Librarian

Sybil takes the information you give it, and gives the information back later when you ask for it.

## Example:

//todo


## Window Install:
```
#cli as admin
pip install --upgrade pip setuptools
pip install virtualenv
pip install virtualenvwrapper-win
mkvirtualenv Sybil
setprojectdir .
pip install flask
setx FLASK_APP sybil.py 
deactivate
# close and re-open cli
```

## To work on the server:
`workon Sybil`

## Deploy Server:
`flask run`

### View server at:
localhost:5000

## Linux Install:
```
sudo pip install virtualenv
```

### Heroku:
#### Install Heroku CLI Toolbelt:
```
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
```

#### Deploy:
```
heroku create
heroku local
heroku keys:add
git push heroku master
heroku open
```