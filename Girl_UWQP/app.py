# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:06:25 2020

@author: kumar
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model=load('random.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output > 80 and output<=100):
        return render_template('index.html', prediction_text='Excellent WQI {:.2f}'.format(output))
    if(output > 50 and output<=80):
        return render_template('index.html', prediction_text='good WQI {:.2f}'.format(output))
    if(output > 20 and output<=50):
        return render_template('index.html', prediction_text='low WQI {:.2f}'.format(output))
    if(output > 0 and output<=20):
        return render_template('index.html', prediction_text='poor WQI {:.2f}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)
