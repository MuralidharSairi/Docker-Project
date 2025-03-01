import os
import re
import socket
from collections import Counter

# Define file paths
data_dir = "/home/data"
file1_path = os.path.join(data_dir, "IF-1.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")
output_path = os.path.join(data_dir, "output/result.txt")

# Function to read file and count words
def count_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        words = re.findall(r"\b\w+(?:'\w+)?\b", file.read().lower())  # Handling contractions
    return words, Counter(words)

# Read files and count words
words1, counter1 = count_words(file1_path)
words2, counter2 = count_words(file2_path)

# Total word counts
total_words_file1 = len(words1)
total_words_file2 = len(words2)
grand_total_words = total_words_file1 + total_words_file2

# Top 3 frequent words
top3_file1 = counter1.most_common(3)
top3_file2 = Counter(word for word in words2 if not re.match(r"\b(?:'s|n't|'re|'ll|'d|'ve|'m)\b", word)).most_common(3)

# Get container IP
try:
    container_ip = socket.gethostbyname(socket.gethostname())
except socket.gaierror:
    # Fallback for Docker Swarm where hostname resolution might fail
    container_ip = "Running in Docker Swarm"

# Prepare results
results = f"""Total words in IF-1.txt: {total_words_file1}
Total words in AlwaysRememberUsThisWay-1.txt: {total_words_file2}
Grand total words: {grand_total_words}

Top 3 words in IF-1.txt:
{top3_file1}

Top 3 words in AlwaysRememberUsThisWay-1.txt (after handling contractions):
{top3_file2}

Container IP Address: {container_ip}
"""

# Create output directory
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write to result.txt
with open(output_path, "w") as out_file:
    out_file.write(results)

# Print results to console
print(results)
