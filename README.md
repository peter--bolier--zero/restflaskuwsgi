


- todo add text.

Folder structure

/
  manifest.yml     - for deployment on bluemix
  Procfile         - process bluemix will initiate (we want to run uwsgi to serve our flask application)
  requirements.txt - python libraries to install, used by pip
  server.ini       - initialisation for uwsgi
  
/service
  adviceapi.py (flask application, skeleton version)
  
/service/templates
  404.html         - page to show 404 
  index.html       - default page
  
/test
  testapi.py       - simpel local test.