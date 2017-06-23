# Warpper for uwsgi. 
from service.adviceapi import app as application
import os

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    application.run(host='0.0.0.0', port = port)
