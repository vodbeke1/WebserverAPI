"""
########3. Web service for storing a list of strings########

We need a webserver application. 

This application is for storing and extending a list of string and for giving us the possibility to get this list back. 

There are two ways how our application can store this list. The first way is to store it on the filesystem (in a file for example) and the second way is to store it “in-memory”. 
The application should decide which way to work with by an argument or an environment variable. It’s up to the developer.

If it is stored in the memory, on every 10. successful PUT request, the list has to be written into a file as a backup. The file name should be given as an environment variable or an argument.

If there are any errors (expected or unexpected) during the requests, the application responses have to contain the information about it with error codes and messages as well.

The application has to handle a PUT and a GET request.
PUT request
It requires one json data structure with a field “item”. It has to append that to the list.
GET request
It needs to return the whole list in json format.
Documentation
We need a documentation that describes how we can build the environment and how to run the application and the (optional) tests.

The documentation must contain the information about how we can communicate with the app.
Restrictions
The “If” and “switch” statements are forbidden to use in all parts of the application except for the tests.

Two equal items cannot be in the “database”.
Bonus tasks (optional)
•	Writing unit and/or integration tests
•	Containerizing the app (Docker) and describing how to build and run
"""

from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request
from flask_env import MetaFlaskEnv

import os
import json
import pickle

# Set environment variable
os.environ['STORE_IN_MEM']='True'

class Configuration(metaclass=MetaFlaskEnv):
    ENV = 'development'
    DEBUG = True

app = Flask(__name__)
app.config.from_object(Configuration)


app_list = []
put_counter = 0

# Initialize empty pickled list
with open('list.pkl', 'wb') as f:
    pickle.dump([], f)






@app.route("/", methods=['GET', 'PUT'])
def fun():
    global app_list
    global put_counter

    store_in_mem = os.getenv('STORE_IN_MEM') == 'True'

    check_get = request.method == 'GET'
    check_put = request.method == 'PUT'
    try:
        # Case if the request is a GET request
        while check_get:
            while store_in_mem:
                return jsonify({'list': app_list})
            with open('list.pkl', 'rb') as f:
                app_list = pickle.load(f)
                return jsonify({'list': app_list})

        # Case if the request is a PUT request
        put_counter += 1
        while check_put:
            while store_in_mem:
                app_list.append(json.loads(request.data)['item'])
                app_list = list(set(app_list))

                while put_counter % 10 == 0:
                    with open('list.pkl', 'wb') as f:
                        pickle.dump(app_list, f)
                    return "ECHO: PUT\n"
                return "ECHO: PUT\n"
                
            with open('list.pkl', 'rb') as f:
                app_list = pickle.load(f)
            app_list.append(json.loads(request.data)['item'])
            app_list = list(set(app_list))

            with open('list.pkl', 'wb') as f:
                pickle.dump(app_list, f)

            return 'ECHO: PUT\n'

        # Case neither GET or PUT request
        return 'ECHO: PUT\n'
    except Exception as e:
        return str(e)

    
if __name__ == '__main__':
    app.run(port='8080')

    






