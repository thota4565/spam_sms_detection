from flask import Flask, render_template, request
import pickle

# Load trained model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        message_tfidf = vectorizer.transform([message])  # Convert text to numerical format
        prediction = model.predict(message_tfidf)[0]  # Predict spam or ham
        result = "Spam" if prediction == 1 else "Ham"
        return render_template("index.html", prediction=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
