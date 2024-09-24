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

### Usage

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/radiologist-consistency-verbiage.git
cd radiologist-consistency-verbiage
```

#### 2. Install dependencies
First, ensure that you have Python 3.8 or higher installed. Then, install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

#### 3. Prepare your data
Ensure you have your 20,000 CT scans and the corresponding radiology reports in the proper format:
- CT Scans should be stored in a folder, with paths specified in the config file.
- Radiology reports should be in text format, processed for use in NLP analysis.

#### 4. Running the YOLOv8 model on the CT scans
To detect coronary artery calcifications using the pre-trained YOLOv8 model, run the following command:
```bash
python yolo_detection.py --input_folder path_to_ct_scans --output_folder results/
```

#### 5. Run Agatston scoring
Once the YOLOv8 model has detected calcifications, the next step is to apply Agatston scoring. Use the following command:
```bash
python agatston_scoring.py --input_folder path_to_yolo_results --output_file agatston_scores.csv
```

#### 6. Analyze radiology report verbiage
Perform Natural Language Processing on the radiology reports to evaluate the consistency of terms describing coronary calcifications:
```bash
python nlp_analysis.py --reports_folder path_to_reports --output_file nlp_results.csv
```

#### 7. Correlate results
Finally, correlate the radiology report verbiage with the Agatston scores and produce a summary report:
```bash
python correlation_analysis.py --nlp_results nlp_results.csv --agatston_scores agatston_scores.csv --output_file final_report.pdf
```
