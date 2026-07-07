# 🌍 Human Development Index (HDI) Prediction System

A Machine Learning-based web application that predicts the **Human Development Index (HDI)** of a country using **Linear Regression**. The application is built with **Flask** and provides an easy-to-use interface where users can enter socio-economic indicators and receive the predicted HDI score along with its development category.

---

## 📖 Project Overview

The **Human Development Index (HDI)** is a composite index developed by the United Nations to measure a country's overall development based on three dimensions:

- Health
- Education
- Standard of Living

This project predicts the HDI using four important indicators:

- Life Expectancy at Birth
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) per Capita

The trained Machine Learning model is integrated with a Flask web application to provide fast and accurate predictions.

---

## 🎯 Objectives

- Predict the Human Development Index accurately.
- Reduce manual calculations.
- Build a simple and user-friendly web application.
- Demonstrate the practical use of Machine Learning.

---

## ✨ Features

- Predicts Human Development Index (HDI)
- Uses Linear Regression Machine Learning model
- User-friendly web interface
- Fast prediction
- Displays HDI score
- Classifies the predicted HDI into:
  - Very High Human Development
  - High Human Development
  - Medium Human Development
  - Low Human Development
- Input validation

---

## 🛠 Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Web Framework
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Model Storage
- Pickle (`HDI.pkl`)

---

## 🤖 Machine Learning Algorithm

**Algorithm Used:** Linear Regression

Linear Regression was selected because it is suitable for predicting continuous numerical values such as the Human Development Index.

---

## 📂 Project Structure

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
│       ├── css/
│       ├── js/
│       └── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ System Requirements

### Hardware

- Intel Core i3 Processor or above
- 4 GB RAM (8 GB Recommended)
- 500 MB Free Disk Space

### Software

- Python 3.10+
- Visual Studio Code
- Jupyter Notebook
- Git (Optional)

---
# 🚀 Installation & Running the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/AP24110010307/HDI-WellBeing-Project.git
```

---

## Step 2: Navigate to the Repository

```bash
cd HDI-WellBeing-Project
```

---

## Step 3: Navigate to the Project Code Folder

### Windows

```bash
cd "5. Project Development Phase\project code files"
```

### Linux / macOS

```bash
cd "5. Project Development Phase/project code files"
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5: Navigate to the Flask Folder

### Windows

```bash
cd flask
```

### Linux / macOS

```bash
cd flask
```

---

## Step 6: Run the Application

```bash
python app.py
```

If Python is installed as `python3`:

```bash
python3 app.py
```

---

## Step 7: Open the Application

Open your browser and visit:

```
http://127.0.0.1:5000
```

The **HDI Prediction System** will start successfully.

---

## 📝 Input Features

The application accepts the following inputs:

- Life Expectancy at Birth
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) per Capita

---

## 📊 Output

The application predicts:

- Human Development Index (HDI)

It also classifies the result into:

- Very High Human Development
- High Human Development
- Medium Human Development
- Low Human Development

---

## 🔄 Workflow

```text
User
   │
   ▼
Enter HDI Parameters
   │
   ▼
Flask Web Application
   │
   ▼
Linear Regression Model (HDI.pkl)
   │
   ▼
Predict HDI
   │
   ▼
Classify Development Category
   │
   ▼
Display Result
```

---

## 📸 Screenshots

### Home Page



---

### Result Page



---

## 📈 Future Enhancements

- Deploy the application on cloud platforms.
- Integrate live HDI datasets.
- Add graphical dashboards and visualizations.
- Compare multiple countries simultaneously.
- Improve prediction accuracy using advanced Machine Learning algorithms such as Random Forest and XGBoost.

---

## 👨‍💻 Team Members

- Santhosh Masupalli
- Praveen Ram
- Chaithu
- Varshit

---

## 📚 Libraries Used

- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle

---

## 📄 License

This project was developed for educational purposes as part of the **APSCHE AI & Machine Learning Internship Program**.

---

## 🙏 Acknowledgement

We sincerely thank **APSCHE**, **SmartBridge**, our mentors, and our faculty members for their continuous guidance and support throughout the development of this project.

---

## ⭐ Project Summary

| Project | Human Development Index (HDI) Prediction System |
|---------|------------------------------------------------|
| Algorithm | Linear Regression |
| Framework | Flask |
| Language | Python |
| Frontend | HTML, CSS, JavaScript |
| Dataset | Human Development Index (HDI) Dataset |
| Output | HDI Score & Development Category |