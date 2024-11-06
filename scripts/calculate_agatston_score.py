import numpy as np

def calculate_agatston(detections):
    agatston_scores = []
    
    for detection in detections:
        # Example: Calculate Agatston score based on area and density of calcifications
        # Simplified logic: assume density is categorized into ranges
        area = detection['area']
        density = detection['density']
        
        if density > 130: 
            agatston_score = area * 1  # Density scaling
        elif density > 200:
            agatston_score = area * 2
        else:
            agatston_score = area * 4
        
        agatston_scores.append(agatston_score)
        
    return np.sum(agatston_scores)

def main():
    detections = load_detections("results/detections/")
    scores = calculate_agatston(detections)
    save_agatston_scores(scores, "results/agatston_scores.csv")

if __name__ == "__main__":
    main()
