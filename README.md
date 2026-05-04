#  Hacker News Engagement Predictor

Live demo: https://ai-sentiment-predictor.streamlit.app

##  Overview

This project predicts whether a Hacker News post title is likely to receive **high engagement** using a machine learning model built with PyTorch.

It covers the full ML lifecycle:

* Data collection
* Preprocessing
* Model training
* Inference pipeline
* API development
* UI deployment with Streamlit

---

##  How it works

1. A post title is input by the user
2. The text is tokenized and converted into numerical form
3. The trained model processes the input
4. A probability score is returned
5. The result is classified as:

   * **High engagement**
   * **Low engagement**

---

##  Tech Stack

* Python
* PyTorch
* Streamlit
* FastAPI (for API layer)
* Pandas / NumPy

---

##  Project Structure

```
ai-product-sentiment-analyzer/
│
├── app/
│   ├── ui.py              # Streamlit UI
│   ├── predict.py         # Inference logic
│   ├── model_utils.py     # Model + preprocessing
│
├── data/
│   ├── data.csv
│   ├── clean_data.csv
│
├── models/
│   ├── model.pt
│   ├── vocab.pt
│
├── notebooks/
│   ├── analysis.ipynb     # Training & experimentation
│
├── scripts/
│   ├── fetch_data.py
│
├── requirements.txt
└── README.md
```

---

##  Run locally

```bash
# clone repo
git clone https://github.com/your-username/ai-product-sentiment-analyzer.git
cd ai-product-sentiment-analyzer

# create environment (optional)
python -m venv venv
.\venv\Scripts\activate   # Windows

# install dependencies
pip install -r requirements.txt

# run app
streamlit run app/ui.py
```

---

##  Example

Input:

```
OpenAI releases new model
```

Output:

```
Probability: 0.61
High engagement 🚀
```

---

##  Limitations

* Model tends to overpredict the positive class
* Limited dataset size
* Simple tokenization (no advanced NLP techniques)
* Uses basic embedding averaging

---

##  Future Improvements

* Use TF-IDF or pretrained embeddings
* Improve dataset size and quality
* Better class balancing
* Add evaluation metrics (precision, recall, F1)
* Experiment tracking and model comparison

---

##  Key Takeaways

This project demonstrates:

* End-to-end ML system design
* Model deployment and serving
* Building user-facing ML applications

---

##  Author

António Pereira
