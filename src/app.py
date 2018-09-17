from apistar import App, Route, http
from apistar.types import Type
from apistar.validators import String


class WelcomeParams(Type):
    name = String(allow_null=True, description="Your name!")

def welcome(params:http.QueryParams) -> dict:
    name = dict(WelcomeParams(**dict(params)))['name']
    print(name)
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', method='GET', handler=welcome),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
