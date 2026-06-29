# 🌍 Human Development Index (HDI) Prediction System

## Project Overview

This project predicts the **Human Development Index (HDI)** of a country using a **Linear Regression Machine Learning model**. The prediction is based on four development indicators:

* Life Expectancy at Birth
* Expected Years of Schooling
* Mean Years of Schooling
* Gross National Income (GNI) per Capita

The project is developed using **Python, Scikit-learn, Pandas, NumPy, and Flask**.

---

# Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* HTML
* CSS
* JavaScript

---

## Project Structure

```text
APSCHE_Project/
│
├── dataset/
│   └── HDI.csv
│
├── training/
│   └── HumanDevIndex.ipynb
│
├── flask/
│   ├── app.py
│   ├── HDI.pkl
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       ├── style.css
│       ├── script.js
│       └── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```


---

# Installation & Running the Project

### Step 1: Clone the Repository

git clone <repository-url>

---

### Step 2: Open the Project Folder

cd APSCHE_Project

---

### Step 3: Install the Required Dependencies

pip install -r requirements.txt

---

### Step 4: Move to the Flask Directory

cd flask

---

### Step 5: Run the Flask Application

python app.py


If `python` doesn't work, use:

python3 app.py

---

### Step 6: Open the Application

Open your web browser and visit:


http://127.0.0.1:5000


The Human Development Index (HDI) Prediction application will now be running locally.


If Python is installed as `python3`, run:


python3 app.py


---

# Open the Application

Open your browser and visit:


http://127.0.0.1:5000


---

# Input Features

* Life Expectancy at Birth
* Expected Years of Schooling
* Mean Years of Schooling
* Gross National Income (GNI) per Capita

---

# Output

The application predicts:

* Human Development Index (HDI)
* HDI Category

  * Very High Human Development
  * High Human Development
  * Medium Human Development
  * Low Human Development

---

# Authors

Developed as part of the APSCHE AI/ML Group Project.
