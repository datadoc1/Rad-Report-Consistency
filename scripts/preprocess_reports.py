import os
import pandas as pd
import csv
from dotenv import load_dotenv
import time
import google.generativeai as genai

def preprocess_report(report_text):
    lines = report_text.split('\n')
    relevant_lines = []
    impression_started = False

    for line in lines:
        if impression_started:
            relevant_lines.append(line)
        elif line.startswith("Great vessels:") or line.startswith("Heart and pericardium:"):
            relevant_lines.append(line)
        elif line.startswith("IMPRESSION:"):
            relevant_lines.append(line)
            impression_started = True

    return '\n'.join(relevant_lines)

if __name__ == "__main__":
    load_dotenv()
    input_directory = 'data/reports'
    output_csv = 'processed_reports.csv'

    api_key = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    data = []

    detection_prompts = {
        'cac': """
        Please analyze this radiology report and determine if a coronary artery or heart calcification (CAC) is mentioned.
        Answer only 'True' if CAC is reported, or 'False' if it is not.
        Report:
        {text}
        """,
        'vessels': """
        Please analyze this radiology report and determine if any great vessel findings are mentioned.
        Answer only 'True' if great vessel findings are reported, or 'False' if not.
        Report:
        {text}
        """
    }

    extraction_prompts = {
        'cac': """
        From the following radiology report, extract only the specific sentences or phrases that mention coronary artery or heart calcification (CAC).
        Return only the relevant text snippets, separated by newlines. If none exist, return "None".
        Report:
        {text}
        """,
        'vessels': """
        From the following radiology report, extract only the specific sentences or phrases that mention great vessel findings.
        Return only the relevant text snippets, separated by newlines. If none exist, return "None".
        Report:
        {text}
        """
    }

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            print(f"Processing file: {filename}")
            with open(os.path.join(input_directory, filename), 'r') as file:
                raw_text = file.read()
                report_text = preprocess_report(raw_text)

            results = {
                'Report Filename': filename,
                'Reported CAC': False,
                'Reported GV': False,
                'Reported CAC text': '',
                'Reported GV text': ''
            }

            # Process both CAC and vessels
            for finding_type in ['cac', 'vessels']:
                # Check if finding is present
                detection_response = model.generate_content(
                    detection_prompts[finding_type].format(text=report_text)
                )
                has_finding = detection_response.text.strip().lower() == 'true'
                results[f'Reported {finding_type.upper()}'] = has_finding
                print(f"{finding_type} detection result for {filename}: {has_finding}")
                time.sleep(5)

                # Extract relevant text if finding is present
                if has_finding:
                    extraction_response = model.generate_content(
                        extraction_prompts[finding_type].format(text=report_text)
                    )
                    results[f'Reported {finding_type.upper()} text'] = extraction_response.text.strip()
                    print(f"{finding_type} extraction result for {filename}: {extraction_response.text.strip()}")
                    time.sleep(5)

            data.append(results)

    # Write results to CSV
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")