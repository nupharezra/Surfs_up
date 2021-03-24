#Import flask dependency
from flask import Flask

#Create a new Flask app instance
app = Flask(__name__)

#Create Flask route
@app.route('/')
# def hello_world():
#     return 'Hello world'

def get_product(name):
  return "The product is " + str(name)

get_product(name='lillian')
