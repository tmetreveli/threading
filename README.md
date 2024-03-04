# Multithreaded JSON Data Fetcher

# Overview
This Python project demonstrates the use of multithreading to efficiently fetch data from the "dummyjson" products API. It creates multiple threads to download product data concurrently and saves the results in a JSON file. This approach significantly reduces the overall data retrieval time compared to a sequential approach.

# Requirements
Python 3.x

# Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the requests library. This project requires requests to make HTTP calls to the API. Install it using pip:
pip install requirements.txt
3. Clone this repository or download the project files to your local machine.

# Usage
python manage.py

# Output
The script saves the fetched data into a file named sample.json. Each entry in the JSON file represents a product's data as returned by the "dummyjson" API. The data is formatted for readability, with each product's information indented.

The console output will display the total time taken to load all the data, providing an insight into the efficiency gained through multithreading.
