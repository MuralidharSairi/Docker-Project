# Project Overview
The Text Analyzer application performs the following tasks:
# Word Count:

Counts the total number of words in two input text files.
Calculates the grand total word count across both files.
Frequency Analysis:

Identifies the top 3 most frequent words in the first file.
Handles contractions (e.g., "I'm", "don't", "can't") by splitting them into individual words and identifies the top 3 most frequent words in the second file.
IP Address:

Retrieves the IP address of the machine running the Docker container.
# Output:

Writes the results (word count, most frequent words, IP address) to a text file inside the container, located at eg: /home/data/output/result.txt.
The results are also printed to the console when the container runs.# Docker-based Text Analyzer Application
This project involves building and deploying a Docker container that analyzes two text files and generates various statistics, such as word count and frequency analysis. The application is packaged into a Docker container for easy deployment, and it processes text files located inside the container.

# Features
Lightweight Docker Image: Built using a minimal base image (such as python:3.9-slim) to ensure fast and efficient deployments.
Automated Process: The container runs automatically without any manual intervention, executes the analysis, generates output, and exits.
Optimized Docker Image: The Docker image is optimized to be under 200MB in size for efficient deployment.
