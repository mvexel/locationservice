locationservice
===============

A minimalist location posting service using Flask

Set it up
---------

Install some prerequisites:

    sudo apt-get install python-dev libapache2-mod-wsgi sqlite3 libsqlite3-dev

Clone this repo:

    git clone https://github.com/mvexel/locationservice.git
    
Create a virtualenv to run this in and add the current path to it:

    mkvirtualenv locationservice
    cd locationservice
    add2virtualenv .
    
Install the python requirements:     

    pip install -r requirements.txt
    
Edit the file `locationservice.conf` and `locationservice.wsgi` so that the path corresponds to where the locationservice app and virtualenv live.
Then add symlink it into the Apache `conf.d` directory:

    sudo ln -s /home/pi/locationservice/locationservice.conf /etc/apache2/sites-enabled/
    
Restart Apache:

    sudo service apache2 restart

Run it 
------

    curl -u admin:secret http://localhost/loc/generate_tables

Use it
------

post a location:

    curl -X POST http://localhost/loc/-111.9208/40.7764/

retrieve a list of locations:

    curl -u admin:secret http://localhost/loc/list
    
Don't forget to change the credentials if you're actually going to use this.
Have fun.
