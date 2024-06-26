from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger
import joblib
import pickle

app = Flask(__name__)
Swagger(app)
# pickle_in = open('classifier.pkl', 'rb')
# classifier = pickle.load(pickle_in)
classifier = joblib.load('classifier2.pkl')

# class CustomUnpickler(pickle.Unpickler):
#     def find_class(self, module, name):
#         if module == 'sklearn.ensemble._forest':
#             module = 'sklearn.ensemble._base'
#         return super().find_class(module, name)

# with open('classifier2.pkl', 'rb') as f:
#     classifier = CustomUnpickler(f).load()

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods = ["Get"])
def predict_note_authentication():
    """Let's Authenticare the Bank Note
    This is using docstrings for specification.
    ---
    parameters:
      - name : variance
        in : query
        type : number
        required : true
      - name : skewness
        in : query
        type : number
        required : true
      - name : curtosis
        in : query
        type : number
        required : true
      - name : entropy
        in : query
        type : number
        required : true
    responses:
        200:
            description : the output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis, entropy]]) 
    return "The predicted value is " + str(prediction)

@app.route('/predict_file', methods = ["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    paramenters:
        - name : file
          in : formData
          type : file
          required : true
    responses:
        200:
            description : The output values
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The predicted values for the csv is " + str(list(prediction))

if __name__ == '__main__':
    app.run()