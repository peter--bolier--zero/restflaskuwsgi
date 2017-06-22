


# TODO finish this text thingy

Folder structure:

```
/
  manifest.yml     - for deployment on bluemix
  Procfile         - process bluemix will initiate (uwsgi to serve flask)
  requirements.txt - python libraries to install, used by pip
  server.ini       - initialisation for uwsgi
  
/service
  adviceapi.py (flask application, skeleton version)
  
/service/templates
  404.html         - page to show 404 
  index.html       - default page
  
/test
  testapi.py       - simpel local test
```

Not all done yet.

Using cloudfoundry to push to bluemix:
- set api to correct region
- ensure correct working directory
- push application to bluemix


