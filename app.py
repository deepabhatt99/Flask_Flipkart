from flask import Flask, render_template, url_for, request
import numpy as np
import pickle
import joblib  # Importing joblib from sklearn.externals
import pandas as pd
import flasgger
from flasgger import Swagger
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
  # Importing joblib from sklearn.externals

app = Flask(__name__)
Swagger(app)

mnb = pickle.load(open('Naive_Bayes_model.pkl', 'rb'))
countVect = pickle.load(open('countVect_imdb.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Reviews = request.form['Reviews']
        data = [Reviews]
        vect = countVect.transform(data).toarray()
        my_prediction = mnb.predict(vect)
    return render_template('results.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)
