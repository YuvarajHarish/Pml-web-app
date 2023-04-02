from flask import Flask, render_template, request
import pickle

# Initialize the Flask application
app = Flask(__name__)

model=pickle.load(open('loan_model .pkl','rb'))


# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the loan prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input data from the form
    gender = request.form['gender']
    married = request.form['married']
    dependents = request.form['dependents']
    education = request.form['education']
    self_employed = request.form['self_employed']
    applicant_income = float(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_amount_term = float(request.form['loan_amount_term'])
    credit_history = float(request.form['credit_history'])
    property_area = request.form['property_area']

    # Make a prediction using the model
    prediction = model.predict(gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)

    # Return the prediction to the user
    return render_template('result.html', prediction=prediction)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
