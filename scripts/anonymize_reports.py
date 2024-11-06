import os

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
    input_directory = 'data/reports'
    output_directory = 'data/anonymized_reports'
    anonymize_reports(input_directory, output_directory)