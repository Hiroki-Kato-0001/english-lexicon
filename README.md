# English Regional Lexicon Detector

## Overview
This project builds a regional English lexicon database and detects
regional characteristics (Brithsh, North American, etc.) from Wikipedia articles using NLP.

## Features
- Raw data created and developed manually using sources from websites and dictionaries, which continues to progress. Downloaded as a CSV file
- CSV → categorized JSON lexicon conversion
- Inflection, phrasal, and root-based matching
- Lemmatization using spaCy
- Wikipedia article analysis

## Setup
pip install -r requirements.txt

## Usage
python main.py