from flask import Flask, render_template, request
from flask_restful import Resource, Api, abort

import atexit
import cf_deployment_tracker
import os
import json

import logging
from logging.handlers import RotatingFileHandler

import datetime

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)
app.debug = False # disable debugging for deployment

api = Api(app)

# TODO expand with required services, i.e. database.
if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')

# --- Service part

# Define specific 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define index, i.e. default page
@app.route('/')
def home():
    return render_template('index.html')




# TODO: Actual call to advice module
def AdviceMe(request):
    advice =  {}
    advice ["value"    ] = 42
    advice ["timestamp"] = datetime.datetime.now().isoformat()
    print(advice)
    return advice

# /* Endpoint to indicate the start of a trip
# * Send a POST request to <see resource below> with body
# * {
# *     "type": 0,
#       ...
# * }
# */
class TripStart(Resource):
    def put(self):
        # TODO: smarter reuse for check of types
        app.logger.debug("TripStart put " + str(request.data))
        if not request.json or not 'type' in request.json:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request {} for endpoint, refusing.'.format(request.json))
        if request.json['type'] != 0:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request type {} for endpoint, refusing.'.format(request.json['type']))

        app.logger.debug(request.get_json())
        return AdviceMe(request)
api.add_resource(TripStart, '/api/V0.2/trip/start') # no parameters

# /* Endpoint to request speed advice, how fast should we go for optimal results?
# * Send a POST request to <see resource below> with body
# * {
# *     "type": 1,
#       ...
# * }
# */
class TripAdviceSpeed(Resource):
    def put(self):
        # TODO: smarter reuse for check of types
        app.logger.debug("TripAdviceSpeed put " + str(request.data))
        if not request.json or not 'type' in request.json:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request {} for endpoint, refusing.'.format(request.json))
        if request.json['type'] != 1:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request type {} for endpoint, refusing.'.format(request.json['type']))
        app.logger.debug(request.get_json())
        return AdviceMe(request)
api.add_resource(TripAdviceSpeed, '/api/V0.1/trip/advice/speed') # no parameters


# /* Endpoint to request parking advice, where should we park for optimal results?
# * Send a POST request to <see resource below> with body
# * {
# *     "type": 2,
#       ...
# * }
# */
class TripAdvicePark(Resource):
    def put(self):
        # TODO: smarter reuse for check of types
        app.logger.debug("TripAdvicePark put " + str(request.data))
        if not request.json or not 'type' in request.json:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request {} for endpoint, refusing.'.format(request.json))
        if request.json['type'] != 2:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request type {} for endpoint, refusing.'.format(request.json['type']))
        return AdviceMe(request)
api.add_resource(TripAdvicePark, '/api/V0.1/trip/advice/park') # no parameters


# /* Endpoint to request charging advice, how fast should we charge for optimal results?
# * Send a POST request to <see resource below> with body
# * {
# *     "type": 3,
#       ...
# * }
# */
class TripAdviceCharge(Resource):
    def put(self):
        # TODO: smarter reuse for check of types
        app.logger.debug("TripAdviceCharge put " + str(request.data))
        if not request.json or not 'type' in request.json:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request for {} endpoint, refusing.'.format(request.json))
        if request.json['type'] != 3:
            app.logger.error("Illegal request " + str(request.data))
            abort(400, message='Illegal request type {} for endpoint, refusing.'.format(request.json['type']))
        return AdviceMe(request)
api.add_resource(TripAdviceCharge, '/api/V0.1/trip/advice/charge') # no parameters


@atexit.register
def shutdown():
    pass # TODO

# Main entry:...
if __name__ == '__main__':
    file_handler = RotatingFileHandler('serviceapi.log', maxBytes=1024 * 1024 *10, backupCount=7)
    file_handler.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(log_formatter)
    app.logger.addHandler(file_handler)

    # default flask setup... hangs once in a while
    #app.run(host='0.0.0.0', port=port, use_debugger=False, debug=True)

    app.logger.info("Advice api main started.")

    #app.debug = True
    port = int(os.getenv('PORT', 5000))
    app.run(port=port, use_debugger=False, debug=False)
