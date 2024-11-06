import os
import shutil
import csv

# Define paths
data_dir = 'data'
raw_data_dir = os.path.join(data_dir, 'raw_data')
scans_dir = os.path.join(data_dir, 'scans')
reports_dir = os.path.join(data_dir, 'reports')
map_file = os.path.join(data_dir, 'file_map.csv')

# Create directories if they don't exist
os.makedirs(scans_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

# Initialize folder number
folder_number = 1

# Open the CSV file to write the map
with open(map_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Folder Number', 'Original Name'])

    # Iterate through each folder in raw_data_dir
    for folder_name in os.listdir(raw_data_dir):
        folder_path = os.path.join(raw_data_dir, folder_name)
        
        if os.path.isdir(folder_path):
            # Find the subfolder within the current folder
            subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
            if subfolders:
                subfolder_name = subfolders[0]
                subfolder_path = os.path.join(folder_path, subfolder_name)
                
                # Define new folder and report paths
                new_folder_name = str(folder_number)
                new_folder_path = os.path.join(scans_dir, new_folder_name)
                new_report_name = f"{new_folder_name}.txt"
                new_report_path = os.path.join(reports_dir, new_report_name)
                
                # Copy the subfolder
                shutil.copytree(subfolder_path, new_folder_path)
                
                # Copy the report.txt file
                report_file_path = os.path.join(folder_path, 'report.txt')
                if os.path.exists(report_file_path):
                    shutil.copy(report_file_path, new_report_path)
                
                # Write the mapping to the CSV file
                writer.writerow([new_folder_name, folder_name])
                
                # Increment folder number
                folder_number += 1
                # Copy all DICOM files from the subfolder to the new location
                for root, _, files in os.walk(subfolder_path):
                    for file in files:
                        if file.lower().endswith('.dcm'):
                            dicom_file_path = os.path.join(root, file)
                            relative_path = os.path.relpath(dicom_file_path, subfolder_path)
                            new_dicom_file_path = os.path.join(new_folder_path, relative_path)
                            os.makedirs(os.path.dirname(new_dicom_file_path), exist_ok=True)
                            shutil.copy(dicom_file_path, new_dicom_file_path)