# Import Required Libraries

from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open("HDI.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    
    # 1. Read user input
    # 2. Convert values into floating-point numbers
    # 3. Create a DataFrame
    # 4. Load the trained model
    # 5. Predict HDI
    # 6. Determine HDI category
    # 7. Display the prediction result


    print(request.form)
    print("Predict route called")
    # Read values entered by the user
    life_expectancy = float(request.form["life_expectancy"])
    expected_schooling = float(request.form["expected_schooling"])
    mean_schooling = float(request.form["mean_schooling"])
    gni = float(request.form["gni"])

    # Create DataFrame with the same feature names used during training
    input_data = pd.DataFrame({
        "Life expectancy at birth": [life_expectancy],
        "Expected years of schooling": [expected_schooling],
        "Mean years of schooling": [mean_schooling],
        "Gross national income (GNI) per capita": [gni]
    })

    prediction = model.predict(input_data)
    predicted_hdi = round(float(prediction[0][0]), 3)

    if predicted_hdi >= 0.800:
        category = "Very High Human Development"

    elif predicted_hdi >= 0.700:
        category = "High Human Development"

    elif predicted_hdi >= 0.550:
        category = "Medium Human Development"

    else:
        category = "Low Human Development"

    return render_template(
        "result.html",
        hdi_score=predicted_hdi,
        category=category
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)