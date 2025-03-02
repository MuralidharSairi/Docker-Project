# Docker-based Text Analyzer Application
This project involves building and deploying a Docker container that analyzes two text files and generates various statistics, such as word count and frequency analysis. The application is packaged into a Docker container for easy deployment, and it processes text files located inside the container.

The Text Analyzer application performs the following tasks:

## Word Count:
Counts the total number of words in two input text files.
Calculates the grand total word count across both files.

## Frequency Analysis:
Identifies the top 3 most frequent words in the first file.
Handles contractions (e.g., "I'm", "don't", "can't") by splitting them into individual words and identifies the top 3 most frequent words in the second file.

## IP Address:
Retrieves the IP address of the machine running the Docker container.

## Output:
Writes the results (word count, most frequent words, IP address) to a text file inside the container, located at eg:/home/data/output/result.txt.
The results are also printed to the console when the container runs.

## Features
Lightweight Docker Image: Built using a minimal base image (such as python:3.9-slim) to ensure fast and efficient deployments.
Automated Process: The container runs automatically without any manual intervention, executes the analysis, generates output, and exits.
Optimized Docker Image: The Docker image is optimized to be under 200MB in size for efficient deployment.

## Steps to Run the Application
Clone this repository to your local machine.

## Build the Docker image:
docker build -t text-analyzer.

## Run the Docker container:
docker run --name text-analyzer -v /path/to/data:/home/data text-analyzer
Replace /path/to/data with the directory on your machine that contains the input text files (e.g., IF-1.txt and AlwaysRememberUsThisWay-1.txt).

## Check the output:
The output file result.txt will be created inside the /home/data directory inside the container.
The results will also be printed to the console when the container is executed.

## Files
IF-1.txt and AlwaysRememberUsThisWay-1.txt: Input text files containing the data to be analyzed.
scripts.py: Python script that performs the word count, frequency analysis, and IP address retrieval.
Dockerfile: Defines the Docker image and sets up the environment to run the Python script.

## Optimizations
Docker Image Size: The Docker image is optimized to be less than 200MB in size to ensure faster builds and deployments.

## Conclusion
This project demonstrates how to build, optimize, and deploy a text-processing application using Docker. The containerized approach ensures that the application is easily portable and can be run consistently on any machine without requiring manual setup.
