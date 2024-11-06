import os
import pandas as pd
import csv
from dotenv import load_dotenv
import time

def preprocess_report(report_text):
    lines = report_text.split('\n')
    relevant_lines = []
    impression_started = False

    for line in lines:
        if impression_started:
            relevant_lines.append(line)
        elif line.startswith("Great vessels:") or line.startswith("Heart and pericardium:") or line.startswith("HISTORY:"):
            relevant_lines.append(line)
        elif line.startswith("IMPRESSION:"):
            relevant_lines.append(line)
            impression_started = True

    return '\n'.join(relevant_lines)

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
            print(f"Processing file: {filename}")
            with open(os.path.join(input_directory, filename), 'r') as file:
                raw_text = file.read()
                report_text = preprocess_report(raw_text)
                
            # First check if CAC is present
            detection_response = model.generate_content(detection_prompt.format(text=report_text))
            has_cac = detection_response.text.strip().lower() == 'true'
            print(f"Detection result for {filename}: {has_cac}")
            time.sleep(5)
            # If CAC is present, extract relevant portions
            if has_cac:
                extraction_response = model.generate_content(extraction_prompt.format(text=report_text))
                relevant_text = extraction_response.text.strip()
                print(f"Extraction result for {filename}: {relevant_text}")
                time.sleep(5)
            else:
                relevant_text = "No CAC mentioned"
                print(f"No CAC mentioned in {filename}")
            
            # Store results
            data.append([filename, has_cac, relevant_text])

    # Create CSV file
    with open('cac_analysis.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Report Filename", "Reported CAC", "Reported Text"])
        writer.writerows(data)
        
    print("Analysis complete. Results saved to cac_analysis.csv")
    output_directory = 'results/reports'