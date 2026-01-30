# English Regional Lexicon Detector

## Overview
This project builds a regional English lexicon database and detects
regional characteristics (British, North American, etc.) in English texts from Wikipedia articles or local TXT/PDF files using NLP techniques.

## Features
- Manually curated raw data based on reliable websites and dictionaries (continuously expanding)
- Raw lexicon data stored and maintained in CSV format
- CSV → categorized JSON lexicon conversion
- Inflection, phrasal, and root-based matching
- Lemmatization using spaCy
- Wikipedia articles and local TXT/PDF file analysis

## Setup
```bash
pip install -r requirements.txt


## Usage
python main.py

## Additional Information
Fetching full articles from Wikipedia may take longer than loading local TXT or PDF files due to API access and network latency.

## Sample Output
**Input**
- Wikipedia article: *Keir Starmer*
- URL: https://en.wikipedia.org/wiki/Keir_Starmer

**Detected regional features (excerpt)**
- British English roots: *cancellation, authorise, programme, bursary, favour, honour, organise, recognise, apologise*, etc.
- North American roots: *honorary, license, jimmy*

**Final Detection Result**
```json
{
  "brit_count": 119,
  "name_count": 1,
  "us_count": 4,
  "can_count": 0,
  "austral_count": 0,
  "nz_count": 0,
  "scot_count": 0,
  "irish_count": 0,
  "ind_count": 0,
  "eafr_count": 0,
  "wafr_count": 0,
  "safr_count": 0,
  "nafr_count": 0,
  "neng_count": 0,
  "easi_count": 0,
  "wasi_count": 0,
  "sasi_count": 0,
  "nasi_count": 0,
  "total": 124
}
Interpretation
Out of 124 regionally identifiable words and phrases, 119 were classified as British English, which is consistent with the article topic (the UK Prime Minister).