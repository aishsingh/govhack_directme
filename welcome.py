# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, render_template, redirect, request
from os.path import abspath, dirname


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__,template_folder=tmpl_dir)


@app.route('/')
def index():
    return render_template("index.html")
    #return app.send_static_file('index.html')

@app.route('/',methods=['POST'])
def my_form_post():

    start = request.form['locationstart']
    end = request.form['locationend']
    start_and_end = [start,end]
    surface_toggle = request.form.getlist('surface')
    injury_toggle = request.form.getlist('injury')
    atmospheric_toggle = request.form.getlist('atmospheric')
    return render_template('map.html',start_pos=start,end_pos=end,
    surface=surface_toggle, injury=injury_toggle, atmospheric=atmospheric_toggle)

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'



@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
