import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def load_agatston_scores(filepath):
    # Load the Agatston scores calculated from YOLOv8 detections
    scores = pd.read_csv(filepath)
    return scores['agatston_score'].values

def load_terminology_data(filepath):
    # Load the preprocessed radiology report terms
    terms = pd.read_csv(filepath)
    return terms['severity'].values  # e.g., 1: mild, 2: moderate, 3: severe

def correlate_scores_terms(agatston_scores, terminology):
    # Compute the Pearson correlation coefficient
    correlation, _ = pearsonr(agatston_scores, terminology)
    return correlation

def main():
    agatston_scores = load_agatston_scores("results/agatston_scores.csv")
    terminology = load_terminology_data("results/terminology_data.csv")
    correlation = correlate_scores_terms(agatston_scores, terminology)
    
    print(f"Pearson correlation: {correlation:.2f}")

if __name__ == "__main__":
    main()
