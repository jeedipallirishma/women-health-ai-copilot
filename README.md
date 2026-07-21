<img width="1909" height="935" alt="Screenshot 2026-07-13 110737" src="https://github.com/user-attachments/assets/1b54830d-ff98-452c-9cde-c1efd372a2ed" />


# Women's Health AI Copilot

An AI-powered healthcare application designed to support women's health awareness through PCOS risk assessment, health analytics, and personalized insights.

![Women's Health AI Copilot](project_screenshot.png)

---

## Project Overview

Women's Health AI Copilot combines survey responses and healthcare datasets to identify potential risk factors associated with PCOS and provide data-driven health insights.

The project focuses on:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* BMI Feature Engineering
* Health Risk Assessment
* AI-Powered Health Assistant (Planned)

---

## Features

* PCOS Risk Assessment
* Health Survey Analysis
* BMI Calculation
* Data Cleaning & Feature Engineering
* Health Analytics Dashboard
* AI-Powered Health Assistant (Planned)

---

## Tech Stack

### Programming & Analysis

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Future Development

* FastAPI
* Streamlit
* Lovable
* Git & GitHub

---

## Dataset Information

The dataset contains women's health survey responses including:

* Age Group
* Height
* Weight
* Menstrual Cycle Regularity
* Severe Period Pain
* Cycle Length
* Sleep Duration
* Physical Activity Level
* Stress Level
* Symptoms Experienced
* Hormonal Disorder History
* Family History of Hormonal Disorders

---

## Data Preprocessing

Completed preprocessing tasks:

### Missing Value Handling

* Filled missing Height values using median imputation.
* Filled missing Weight values using median imputation.
* Filled missing symptom values with "No Symptoms Reported".
* Filled diagnosis values with "Not Diagnosed".

### Data Cleaning

* Converted Height and Weight columns to numeric format.
* Standardized mixed height units (feet to centimeters).
* Removed invalid height records.
* Validated healthcare survey responses.

### Feature Engineering

* Calculated Body Mass Index (BMI).
* Created clean analytical dataset for EDA and future machine learning models.

---

## Exploratory Data Analysis (EDA)

Performed exploratory analysis on cleaned survey data.

### Visualizations Created

* BMI Distribution
* Age Group Distribution
* Menstrual Cycle Regularity Analysis
* Severe Period Pain Analysis
* Family History Analysis
* Physical Activity Analysis
* Stress Level Distribution
* BMI vs Stress Level
* Height vs Weight Relationship
* Correlation Heatmap

### Key Insights

* Identified BMI distribution across participants.
* Analyzed relationships between lifestyle factors and health indicators.
* Explored trends in menstrual health and hormonal disorder history.
* Investigated associations between stress, activity levels, and BMI.

---

## Current Status

### Completed

* Survey dataset collection
* Data cleaning
* Missing value handling
* Height unit standardization
* BMI feature engineering
* Exploratory Data Analysis (EDA)
* GitHub project documentation

### In Progress

* Health Risk Scoring System
* PCOS Risk Assessment Logic
* AI Copilot Architecture Design

### Planned

* Machine Learning Model Development
* Streamlit Dashboard
* FastAPI Backend
* AI Health Assistant
* Personalized Recommendations
* Web Application Deployment

---

## Project Structure

```text
Women's-Health-AI-Copilot/
│
├── data_preprocessing.py
├── survey_data.csv
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── bmi_distribution.png
│   ├── stress_analysis.png
│   ├── age_group_distribution.png
│   ├── correlation_heatmap.png
│
└── future_modules/
```

---

## Future Enhancements

* PCOS Prediction Model
* Explainable AI for Health Insights
* Conversational Health Assistant
* Personalized Wellness Recommendations
* Interactive Analytics Dashboard
* Healthcare Report Generation

---

## Author

### Jeedipalli Rishma

AI & Data Science Enthusiast | Data Analytics | Machine Learning

* LinkedIn: https://www.linkedin.com/in/jeedipallirishma/
* GitHub: https://github.com/jeedipallirishma
* Portfolio: https://rishma-portfolio.framer.website

---

## Status

🚧 Active Development

This project is continuously evolving as part of my AI, Data Science, and Healthcare Analytics learning journey.

