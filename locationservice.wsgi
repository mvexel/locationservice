activate_this = '/home/pi/.virtualenvs/locationservice/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from locationservice import app as application
