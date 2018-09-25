import falcon
import json
import requests
from requests.auth import HTTPBasicAuth
from mongoengine import connect

connect('sheriff', host='mongodb', port=27017)

COMMCARE_USERNAME = os.environ.get('COMMCARE_USERNAME')
COMMCARE_PASSWORD = os.environ.get('COMMCARE_PASSWORD')
CASES_URL = 'https://www.commcarehq.org/a/billy-excerpt/api/v0.5/case/'

class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'hello': 'world',
        }

        cases = requests.get(CASES_URL, auth=HTTPBasicAuth(COMMCARE_USERNAME, COMMCARE_PASSWORD))

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200


api = application = falcon.API()

hello_resource = Resource()
api.add_route('/', hello_resource)
