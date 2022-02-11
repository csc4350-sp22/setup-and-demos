# Lecture 5 Demo - NYT API

This demo explains how to call the New York Times API using the Python requests library and parse its JSON data.
It also shows how you can store and hide your API keys with a `.env` file and `.gitignore` file, respectively.

## Requirements
1. `pip install python-dotenv`
2. `pip install requests`

## Setup
1. Create `.env` file in your main directory
2. Add your NYT key from https://developer.nytimes.com/my-apps with the line: `export NYT_KEY='YOUR_KEY'`

## Run Application
1. Run command in terminal `python lect5-demo.py`
2. See output with list of Gamestop articles 

