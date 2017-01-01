# example_flask.py
'This is an example for the flask application which will make the\
DS suite as the model and hence construct a webapp based on that model.'

from flask import Flask
from flask import request
from flask import render_template

from example import build_linked_list

# initialize the application with the name of the module
# when this module is running as __main__, the '__main__'
# will be passed to Flask and it will be the name of the applcation
# else it is going to be example_flask, since that is what the name of the 
# module(python file) is.

# application is the Flask instance, so it is the webserver (my hyposthesis)
# it acts as the central object and implements the WSGI application.
application = Flask(__name__)


# @application.route('/') is a decorator used to register index() as a view
# function that is called when '/' URL is invoked.
# Hence, example_flask.py becomes the Controller for the application.
@application.route('/')
def index():
  'this is the index or root of our URL a.k.a home'
  return render_template('index.html')

@application.route('/list')
def linked_lists():
  'for testing out my linked lists'
  list_of_items = request.args.get('a').split(',')
  # print('incoming requests = %s' % request)
  l = build_linked_list(list_of_items)
  return render_template('lists.html', passed_list=l)


# if this module is run as the main module, we start the applcation
# server.
if __name__ == '__main__':
  application.run()
