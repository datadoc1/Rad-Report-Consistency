import os
import pandas as pd
import csv
from dotenv import load_dotenv
import time

def anonymize_reports(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(input_dir, filename), 'r') as file:
                lines = file.readlines()

            with open(os.path.join(output_dir, filename), 'w') as file:
                for line in lines:
                    if "REFERRING PHYSICIAN" not in line and "Electronically signed by" not in line:
                        file.write(line)

if __name__ == "__main__":
    load_dotenv()
    input_directory = 'data/reports'
    import google.generativeai as genai

    api_key = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    data = []
    detection_prompt = """
    Please analyze this radiology report and determine if a coronary artery or heart calcification (CAC) is mentioned.
    Answer only 'True' if CAC is reported, or 'False' if it is not.
    Report:
    {text}
    """

    extraction_prompt = """
    From the following radiology report, extract only the specific sentences or phrases that mention coronary artery or heart calcification (CAC).
    Return only the relevant text snippets, separated by newlines. If none exist, return "None".
    Report:
    {text}
    """

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            with open(os.path.join(input_directory, filename), 'r') as file:
                report_text = file.read()
                
            # First check if CAC is present
            detection_response = model.generate_content(detection_prompt.format(text=report_text))
            has_cac = detection_response.text.strip().lower() == 'true'
            time.sleep(5)
            # If CAC is present, extract relevant portions
            if has_cac:
                extraction_response = model.generate_content(extraction_prompt.format(text=report_text))
                relevant_text = extraction_response.text.strip()
                time.sleep(5)
            else:
                relevant_text = "No CAC mentioned"
            
            # Store results
            data.append([filename, has_cac, relevant_text])

    # Create CSV file
    with open('cac_analysis.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Report Filename", "Reported CAC", "Reported Text"])
        writer.writerows(data)
        
    output_directory = 'results/reports'
    anonymize_reports(input_directory, output_directory)