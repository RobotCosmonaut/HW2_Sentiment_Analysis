#
#   CS 7319 Software Architecture
#   Homework 2A
#   Single-Program Architecture via Python
#   Ron Denny
#   rdenny@smu.edu
#   
#   This script was created in Microsoft VSCode and Google Gemini was referenced/utilized in the script development
#

#Import libary for reading from command line
import sys
import os

#Import libraries for plots
import numpy as np
import matplotlib.pyplot as plt

# Define the keyword sets for sentiment analysis
positive_keywords = {'happy', 'excited', 'thrilled', 'love'}
negative_keywords = {'sad', 'depressed', 'angry', 'upset'}

# Initialize counters for the sentiment analysis
classification_counts = {
    "Positive": 0,
    "Negative": 0,
    "Mixed": 0,
    "Neutral": 0
}

# Start of File path logic
# Check if a command-line argument was provided
if len(sys.argv) < 2:
    print("Usage: python Single_Program_Architecture_part_a.py <file_path>")
    sys.exit(1) # Exit with an error code

# Get the file path from the command-line arguments
file_path = sys.argv[1]

# Check if the file exists before attempting to open it
if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found.")
    sys.exit(1) # Exit with an error code
# End of File path logic

# Open and process the file
# READING
with open(file_path, "r") as file:
    for line in file:
        # Tokenize the line case-insensitively and remove apostrophes
        # TOKENIZING
        modified_line = line.strip().lower().replace("'", "")
        tokens = modified_line.split()

        # Check for the presence of positive and negative keywords
        # CLASSIFICATION
        has_positive = any(token in positive_keywords for token in tokens)
        has_negative = any(token in negative_keywords for token in tokens)

        # Classify and increment the appropriate counter
        # TALLYING
        if has_positive and not has_negative:
            classification_counts["Positive"] += 1
        elif has_negative and not has_positive:
            classification_counts["Negative"] += 1
        elif has_positive and has_negative:
            classification_counts["Mixed"] += 1
        else:
            classification_counts["Neutral"] += 1

# Print the summary of counts to the terminal
print(f"Positive={classification_counts['Positive']} Negative={classification_counts['Negative']} Mixed={classification_counts['Mixed']} Neutral={classification_counts['Neutral']}")
     
# Determine the overall verdict
positive_count = classification_counts["Positive"]
negative_count = classification_counts["Negative"]

if positive_count > negative_count:
    verdict = "Happier"
elif negative_count > positive_count:
    verdict = "Sadder"
else:
    verdict = "Tied"

# Print the sentiment analysis verdict to the terminal
print(f"Verdict: {verdict}")

# Plot the counter values via a bar chart
x_values = np.array(["Positive", "Negative", "Mixed", "Neutral"])
y_values = np.array([classification_counts['Positive'], classification_counts['Negative'], classification_counts['Mixed'], classification_counts['Neutral']])
colors = ["lightgreen", "red", "orange", "grey"]
plt.bar(x_values, y_values, color=colors)
plt.show()
