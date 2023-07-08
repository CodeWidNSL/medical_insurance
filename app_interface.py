from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import MedicalInsurance
import config
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_charges', methods=['GET', 'POST'])
def predict_charges():
    try:
        if request.method == 'POST':
            data = request.form
        elif request.method == 'GET':
            data = request.args

        age = int(data['age'])
        gender = data['gender']
        bmi = int(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker']
        region = data['region']

        obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        pred_charges = obj.get_predicted_charges()
        return render_template('index.html', prediction = pred_charges)
    except:
        print(traceback.print_exc())
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080)

