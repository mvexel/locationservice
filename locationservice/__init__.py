from flask import Flask, jsonify, request, Response
from functools import wraps
import datetime, time
from pysqlite2 import dbapi2 as sqlite3

app = Flask(__name__)
app.config.from_object('locationservice.settings')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    file_handler = TimedRotatingFileHandler(
        '/home/pi/log.txt',
        'D')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.debug('logging enabled')

# http://flask.pocoo.org/snippets/8/
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
    
def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == app.config['HTTP_USER'] and password == app.config['HTTP_PASSWORD']

@app.route('/generate_tables', methods=['GET'])
@requires_auth
def generate_tables():
    conn = sqlite3.connect(app.config['SQLITE_PATH'])
    c = conn.cursor()
    c.execute('drop table if exists locations')
    c.execute('create table locations (tstamp date, ip text, lon real, lat real)') 
    return jsonify({'result':'OK'});

@app.route('/<lon>/<lat>', methods=['POST','GET'])
def post_location(lon, lat):
    app.logger.debug(lon, lat)
    conn = sqlite3.connect(app.config['SQLITE_PATH'])
    c = conn.cursor()
    c.execute('insert into locations values (?, ?, ?, ?)' , (datetime.datetime.now(), request.remote_addr, lon, lat))
    conn.commit()
    return jsonify({'result':'OK'});

@app.route('/list', methods=['GET'])
@requires_auth
def get_locations():
    conn = sqlite3.connect(app.config['SQLITE_PATH'])
    c = conn.cursor()
    locations = [row for row in c.execute('select * from locations')]
    return jsonify({'locations': locations})

if __name__ == '__main__':
    app.run()
