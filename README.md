# 📩 Spam SMS Detection - Flask Web App

## 🚀 Project Overview
This project is a **Flask-based web application** that classifies SMS messages as **Spam or Ham (Not Spam)** using a trained **Machine Learning model**.

## 📊 Dataset Information
- The dataset is sourced from **[Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)**.
- It contains **5,572 labeled SMS messages** (Spam or Ham).

## 🏗️ Steps Performed
1️⃣ **Data Preprocessing** (Stopword Removal, Tokenization, TF-IDF Vectorization).  
2️⃣ **Feature Extraction** using **TF-IDF Vectorizer**.  
3️⃣ **Trained Machine Learning Models** (Naïve Bayes, Logistic Regression, Random Forest, SVM).  
4️⃣ **Best Model: Optimized Random Forest (97.49% Accuracy)**.  
5️⃣ **Flask Web App for Real-time SMS Classification**.  

## 🔧 Running the Flask App Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2.Start the Flask app:

    python app.py
3. Open your browser and visit:
     
     http://127.0.0.1:5000/