
# 🧠 Intelligent Sentiment Analysis System

## 📌 Overview
The **Intelligent Sentiment Analysis System** is a Python-based Natural Language Processing (NLP) application designed to analyze textual feedback such as customer reviews, comments, or survey responses and classify them into **Positive, Negative, or Neutral** sentiment categories.

The project is built using a **modular, production-style architecture**, simulating how real-world AI/NLP systems are designed in industry. It focuses on clean code, separation of concerns, and explainability rather than black-box models.

---

## 🎯 Objectives
- Analyze unstructured text data using NLP techniques
- Determine sentiment polarity and confidence score
- Demonstrate an end-to-end AI text processing pipeline
- Apply clean software engineering principles

---

## ✨ Key Features
- Text preprocessing (normalization, noise removal, stopword filtering)
- Sentiment polarity analysis using NLP
- Confidence score calculation
- Modular pipeline architecture
- Centralized logging system
- Input validation and formatted reporting
- Easy to extend with ML models or web interfaces

---

## 🧩 System Architecture
```
User Input
   ↓
Text Preprocessing
   ↓
Sentiment Polarity Scoring
   ↓
Sentiment Classification
   ↓
Confidence Estimation
   ↓
Formatted Output
```

---

## 📁 Project Structure
```
Intelligent_Sentiment_Analysis_System/
│── app.py
│── requirements.txt
│── README.md
│
└── src/
    ├── pipeline.py
    ├── preprocessing.py
    ├── sentiment_model.py
    ├── logger.py
    └── utils.py
```

---

## 🛠️ Technologies Used
- Python
- Natural Language Processing (NLP)
- TextBlob
- Regular Expressions
- Modular Software Design

---

## ▶️ How to Run the Project

### Step 1: Clone the repository
```
git clone <repository-url>
cd Intelligent_Sentiment_Analysis_System
```

### Step 2: Install dependencies
```
pip install -r requirements.txt
```

### Step 3: Run the application
```
python app.py
```

### Step 4: Use the system
- Enter any customer review or feedback text
- Type `exit` to terminate the program

---

## 📊 Sample Output
```
--- Sentiment Analysis Report ---
Original Text : The service was fast and very reliable
Cleaned Text  : service fast very reliable
Sentiment     : Positive
Polarity      : 0.72
Confidence    : 0.72
--------------------------------
```

---

## 🎓 Learning Outcomes
- Practical understanding of NLP pipelines
- Experience with sentiment polarity and confidence scoring
- Writing clean, modular, and maintainable Python code
- Applying logging and validation in AI systems
- Bridging AI concepts with real-world applications

---

## 🚀 Future Enhancements
- Integrate machine learning–based sentiment models
- Add support for batch input (CSV / text files)
- Build a web interface using Streamlit or Flask
- Add data visualization dashboards
- Improve preprocessing with lemmatization and embeddings

---

## 👤 Author
**Gargi Rami**  
Master of Applied Computing  
University of Windsor  

---

## 📄 License
This project is intended for educational and academic demonstration purposes.
