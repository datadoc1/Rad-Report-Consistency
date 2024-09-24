# Rad-Report-Consistency

# Evaluating Consistency in Radiologist Verbiage for Coronary Calcification

## Project Overview
This project evaluates the consistency in radiologist verbiage when describing coronary calcification and compares it to automated detection and quantification using YOLOv8 and Agatston Scoring on non-contrast chest CT scans.

### Key Steps:
- **YOLOv8 Detection**: Apply a pre-trained YOLOv8 model to detect calcifications.
- **Agatston Scoring**: Compute Agatston scores based on detected calcifications.
- **NLP Analysis**: Use NLP to analyze radiologist reports for terminology consistency.
- **Statistical Correlation**: Compare subjective descriptions to quantitative Agatston scores.

## Repository Structure
- `data/`: Contains radiology reports and CT scan metadata.
- `models/`: YOLOv8 weights and NLP models.
- `notebooks/`: Jupyter notebooks for data exploration.
- `scripts/`: Python scripts for CT scan analysis, Agatston scoring, and NLP processing.
- `results/`: Output files such as detection results, Agatston scores, and correlation analysis.

## Requirements
Install dependencies:
```bash
pip install -r requirements.txt
