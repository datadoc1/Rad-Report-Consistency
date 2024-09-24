import re
import spacy

nlp = spacy.load("en_core_sci_md")  # Load medical-specific language model

def clean_text(text):
    # Remove unnecessary characters, lowercase text
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    return text

def extract_cac_terms(report):
    # Process the report using Spacy NLP
    doc = nlp(report)
    cac_terms = []
    
    for token in doc:
        if token.text in ["calcification", "mild", "moderate", "severe"]:
            cac_terms.append(token.text)
    
    return cac_terms

def preprocess_reports(report_path):
    with open(report_path, 'r') as file:
        report = file.read()
    clean_report = clean_text(report)
    return extract_cac_terms(clean_report)

def main():
    reports_dir = "data/reports/"
    for report_file in os.listdir(reports_dir):
        terms = preprocess_reports(os.path.join(reports_dir, report_file))
        print(terms)  # Later, save this data for further analysis

if __name__ == "__main__":
    main()
