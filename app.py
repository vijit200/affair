from cProfile import label
import numpy as np
from flask import Flask,request,render_template
import pickle
model = pickle.load(open('affair1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])

def predict():
    label = {0:'no',1:'yes'}
    if request.method == 'POST':
        rate_marriage = float(request.form['rate_marriage'])
        age = float(request.form['age'])
        yrs_married= float(request.form['yrs_married'])
        children = float(request.form['children'])
        religious = float(request.form['religious'])
        educ = float(request.form['educ'])
        l = [rate_marriage, age, yrs_married, children, religious, educ]
        model_eval = model.predict([l])[0]
        return  render_template('index.html',predection_eval = label[model_eval])

if __name__ == '__main__':
    app.run(debug=True)