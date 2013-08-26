locationservice
===============

A minimalist location posting service using Flask

Set it up
---------

Install some prerequisites:

    sudo apt-get install python-dev libapache2-mod-wsgi sqlite3 libsqlite3-dev

Clone this repo:

    git clone https://github.com/mvexel/locationservice.git
    
Create a virtualenv to run this in:

    mkvirtualenv locationservice
    
Create a configuration file (or copy the example and adapt to your environment)

    cd locationservice
    cp locationservice/settings_example.py locationservice/settings.py

Install the app and dependencies:

    python setup.py install

Edit the file `apache/locationservice.conf` and `wsgi/locationservice.wsgi` so that the path corresponds to where the locationservice app and virtualenv live.
Then add symlink it into the Apache `sites-enabled` directory:

    sudo ln -s /path/to/locationservice/wsgilocationservice.conf /etc/apache2/sites-enabled/
    
Restart Apache:

    sudo service apache2 restart

Finally, generate the SQLite database file:

    curl -u admin:secret http://localhost/loc/generate_tables


Use it
------

post a location:

    curl -X POST http://localhost/loc/-111.9208/40.7764/

retrieve a list of locations:

    curl -u admin:secret http://localhost/loc/list
    
Don't forget to change the credentials if you're actually going to use this.
Have fun.
