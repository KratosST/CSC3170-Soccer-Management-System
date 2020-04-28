# CSC3170 Group Project

Summary:

This is a soccer database with data from FIFA.

------

Commands to clone and pull: 

git clone https://github.com/kratosst/kratosst.github.io

After clone this porject, just run the following command to pull the updates:

`git pull origin master`



Commands to pull and commit: 

`git add .`

`git commit -m "message"`

`git push -u origin master`

------

Commands to run fifa project by Flask:

Change to the directory where fifa locates, and make sure Flask, pymysql and cryptography and installed:

`pip install Flask`

`pip install pymysql`

`pip install cryptography`

Then set the environment variables:

`export FLASK_APP=fifa`

`export FLASK_ENV=development`

Run the Flask app:

`flask run (or python3 -m flask run)` 

