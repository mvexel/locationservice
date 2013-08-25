locationservice
===============

A minimalist location posting service using Flask

Set it up
---------

    git clone git@github.com:mvexel/locationservice.git
    mkvirtualenv locationservice
    pip install -r requirements.txt

Run it 
------

    python app.py
    curl -u admin:secret http://localhost:5000/generate_tables

Use it
------

post a location:

    curl -X POST http://localhost:5000/-111.9208/40.7764/

retrieve a list of locations:

    curl http://localhost:5000/locations
    
    
Have fun.
