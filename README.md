# Clothing Shop Sales and Customer Feedback Assistant

AI for Everyone **Project 02**, built only from the supplied `Project_02` dataset pack.

**Live demo:** ADD-YOUR-STREAMLIT-LINK-HERE

## What the app does (five tabs)
1. **Shop overview & demand estimate** - charts of the training rows and a form (last-week units, price, discount, footfall, category) that estimates next-week units with a decision tree.
2. **Product profiles** - three KMeans product-planning groups with original-unit averages.
3. **Product image** - a small CNN suggests top / trouser / bag; the owner can correct the category.
4. **Customer comments** - NLTK VADER sentiment and keyword topics for the 30 supplied comments.
5. **Weekly shop review** - an Offline summary (no API key needed) and an optional Groq Free Plan summary.

## Important limits
- The sales table is generated classroom data. Predictions are demonstration estimates, not confirmed sales forecasts or profit advice.
- The clustering groups are product-planning scenarios, not customer segments; group numbers are arbitrary.
- The image model is trained on Fashion MNIST (28x28 grayscale). It may fail on coloured phone photos, several garments or other products. Scores are not calibrated probabilities.
- VADER is an English lexicon method: negation, sarcasm, mixed opinions, Urdu and Roman Urdu are limitations.
- The app only loads saved models. It never trains after a click.

## Repository layout
```text
app.py
requirements.txt
README.md
.gitignore
models/       supervised.joblib, clusters.joblib, images.keras, group_descriptions.json
data/         main.csv, feedback.csv, example_inputs.csv, meta.json, topic_keywords.json, prompt_test_cases.json
sample_images/
nltk_data/    offline VADER lexicon (no download at startup)
source_notices/
notebooks/    Clothing_Shop_Full_Workflow.ipynb (upload it here yourself)
```
`data/images.npz` (full training images), ZIP files and `.streamlit/secrets.toml` are deliberately **not** in this repository.

## Train the models (Google Colab, free)
1. Open `notebooks/Clothing_Shop_Full_Workflow.ipynb` in Google Colab.
2. Run all cells and upload `AI_for_Everyone_Ready_Datasets.zip` when asked.
3. The last cell downloads `Clothing-Shop-Deployment.zip` with everything in this repository.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (free)
1. Create a GitHub Free repository and upload these files with *Add file -> Upload files*.
2. In Streamlit Community Cloud choose *Create app*, select this repository, branch `main`, file `app.py`.
3. In *Advanced settings* choose Python 3.13 (the version used for training).
4. Optional: in *Settings -> Secrets* add
```toml
GROQ_API_KEY = "your-key"
GROQ_MODEL = "openai/gpt-oss-20b"
```
Keep Groq on the free plan. Without a key the app works in Offline summary mode.

## Library versions used for training
```text
pandas==2.2.3
numpy==2.4.6
scikit-learn==1.6.1
joblib==1.6.0
tensorflow-cpu==2.21.0
nltk==3.9.1
streamlit
pillow
plotly
groq
Python 3.13
```
