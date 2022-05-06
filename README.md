> The [sibyls](https://en.wikipedia.org/wiki/Sibyl) were prophetesses or oracles in Ancient Greece.
# Sybil
Is A Natural Language Librarian.
Sybil takes the information you give it, and gives the information back later when you ask for it.

This was my first python project for my AI Class. It includes some rudimentary sentiment analysis, and, astoundingly, a facebook messenger integreation.  I'm not sure how I got this working within 2 weeks. Like all old projects, the code is pretty bad. I know I can do better now.

## Running Locally:
`python analyze.py`

(make sure that `Testing()` is uncommented)

## Windows Dev Install:
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
```
close and re-open cli

## To work on the server:
`workon Sybil`

## Run Server:
`flask run`

### View server at:
localhost:5000

## Heroku:

### Install Heroku CLI Toolbelt:
```
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
```

### Deploy:
Uncomment

```
heroku create
heroku local
heroku keys:add
git push heroku master
heroku open
```
