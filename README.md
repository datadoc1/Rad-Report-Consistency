# Rad-Report-Consistency

## Evaluating Consistency in Radiologist Verbiage for Coronary Calcification

### Project Overview
This project assesses the consistency in radiologist verbiage describing coronary artery calcification (CAC) in non-contrast chest CT scans. The consistency of subjective radiologist reports is compared with quantitative calcification detection using the YOLOv8 model and Agatston Scoring.

### Key Steps:
- **YOLOv8 Detection**: Use a pre-trained YOLOv8 model to detect coronary calcifications.
- **Agatston Scoring**: Compute Agatston scores based on detected calcifications.
- **NLP Analysis**: Apply natural language processing (NLP) to evaluate the consistency of terms used by radiologists in their reports.
- **Statistical Correlation**: Compare the subjective descriptions in reports with the objective Agatston scores.

## Repository Structure
- `data/`: Contains raw data, including radiology reports and metadata of CT scans.
- `models/`: Pre-trained YOLOv8 weights and NLP models used for detection and report analysis.
- `notebooks/`: Jupyter notebooks for exploring and analyzing the data.
- `scripts/`: Python scripts for CT scan analysis, Agatston scoring, and NLP tasks.
- `results/`: Output files including detection results, Agatston scores, and correlation analysis.

## End Goal
The end goal of this project is to produce academic papers across three domains: Coronary Artery Calcifications (CAC), Mitral Valve Calcifications, and Thoracic Aorta Calcifications.

You can review the type of academic paper this project aims to produce for the **Coronary Artery Calcification (CAC)** domain by following this link:

[Evaluating Consistency in Radiologist Verbiage for Coronary Calcification with YOLOv8 Detection and Agatston Scoring](https://docs.google.com/document/d/1qy1QdEzOeG02j8d_3BSurMu_xPFWHbEnP1vC8Xp-1zk/edit)

### Placeholder for Future Papers
- Mitral Valve Calcification (MVC): Paper outline coming soon.
- Thoracic Aorta Calcification (TAC): Paper outline coming soon.

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/rad-report-consistency.git
cd rad-report-consistency
```

### 2. Install dependencies
Ensure that you are using Python 3.8 or higher. Install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Prepare your data
Ensure that the dataset of 20,000 non-contrast chest CT scans and corresponding radiology reports is available and organized:
- **CT Scans**: Place your CT scan data in a folder, and update paths in the configuration file.
- **Radiology Reports**: Store all radiology reports in plain text format for NLP processing.

### 4. Running the YOLOv8 model on CT scans
To detect coronary artery calcifications using the YOLOv8 model, run the following command:
```bash
python scripts/yolo_detection.py --input_folder path_to_ct_scans --output_folder results/yolo_outputs/
```

### 5. Perform Agatston Scoring
After detecting calcifications, perform Agatston scoring based on the results of the YOLOv8 model:
```bash
python scripts/agatston_scoring.py --input_folder results/yolo_outputs --output_file results/agatston_scores.csv
```

### 6. Analyze Radiology Report Verbiage
Use NLP to assess the consistency and terminology used by radiologists in the reports:
```bash
python scripts/nlp_analysis.py --reports_folder path_to_reports --output_file results/nlp_results.csv
```

### 7. Correlate Results
Finally, correlate the verbiage used in the reports with the Agatston scores:
```bash
python scripts/correlation_analysis.py --nlp_results results/nlp_results.csv --agatston_scores results/agatston_scores.csv --output_file results/final_report.pdf
```
