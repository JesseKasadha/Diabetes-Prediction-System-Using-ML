#from importlib.resources import path
from flask import Flask , render_template , request
import numpy as np
import pickle
#from pathlib import Path
#import joblib
#import os

app = Flask(__name__)
model_path = r"C:/Users/Jesse/Desktop/Diabetes/diabetes_prediction.pkl"
model_path = pickle.load(open(model_path, 'rb'))
#model_path = joblib.load(model_path)

#
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detail", methods = ["POST"])
def submit():
    # Html to py
    if request.method == "POST":
        name = request.form["Username"]

    return render_template("detail.html", n = name)


@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bloodpressure = int(request.form['bloodpressure'])
        skinthickness = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetespedigreefunction = float(request.form['diabetespedigreefunction'])
        age = int(request.form['age'])
        
        values = np.array([[pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]])
        prediction = model_path.predict(values)
        
        return render_template('predict.html', prediction=prediction)
    

if __name__=="__main__":
    app.run(debug=False)

