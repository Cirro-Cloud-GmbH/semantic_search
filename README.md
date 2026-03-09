# Semantic Search Demo (Streamlit + FAISS)

This project is a semantic search demo using software requirements dataset.
It uses:
- `sentence-transformers` to create text embeddings
- `FAISS` to build a vector index
- `Streamlit` for the web UI

## What the code does

### 1) Dataset preparation (`prepare_dataset.py`)
- Downloads the source ARFF file from Zenodo.
- Prepares data.
- Saves extracted requirements to `output.txt` (one requirement per line).
- If `output.txt` already exists, preparation is skipped.

### 2) Search app (`app.py`)
- On startup, ensures dataset is prepared (`ensure_data_ready`).
- Loads requirements from `output.txt`.
- Loads embedding model `all-MiniLM-L6-v2`.
- Builds a FAISS cosine-similarity index (normalized vectors + inner product).
- Accepts a query in Streamlit UI and returns top-K most similar requirements.

## Run locally

### Prerequisites
- Python 3.10+ (recommended)
- `pip`

### Steps
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Start the app:
```bash
streamlit run app.py
```
3. Open the local URL printed by Streamlit (usually `http://localhost:8501`).

Notes:
- On first run, the app downloads and prepares the dataset automatically.
- First launch can take longer because the embedding model is downloaded.

## Deploy on Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. Go to Streamlit Community Cloud and create a new app.
3. Select your repository, branch, and set `app.py` as the main file.
4. Deploy.

The platform will install `requirements.txt` automatically.
No secrets are required for this demo.

## Hosted app

Live app:
- https://ci-cloud.streamlit.app/

## Dataset source and license

Dataset used in the demo comes from:
- https://doi.org/10.5281/zenodo.12805484

and is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

## Project files

- `app.py` - Streamlit app and semantic search pipeline.
- `prepare_dataset.py` - download + transform dataset script.
- `requirements.txt` - Python dependencies.
