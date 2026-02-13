CREATE DATABASE IF NOT EXISTS english_lexicon;
USE english_lexicon;

CREATE TABLE regions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10) UNIQUE,
    name VARCHAR(50)
);

CREATE TABLE lexicon_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(255),
    entry_type ENUM('root', 'inflection', 'phrase'),
    region_id INT,
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

CREATE TABLE analysis_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    region_code VARCHAR(10),
    count INT,
    analyzed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
