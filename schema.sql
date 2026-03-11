CREATE DATABASE IF NOT EXISTS english_lexicon;
USE english_lexicon;

CREATE TABLE regions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE entry_types (
	id INT AUTO_INCREMENT PRIMARY KEY,
	code VARCHAR(20) UNIQUE NOT NULL,
    name varchar(20) NOT NULL
);

CREATE TABLE sources (
	id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE lexicon_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(255) NOT NULL,
    entry_type_id INT NOT NULL,
    region_id INT NOT NULL,
    source_id INT NOT NULL,
    note VARCHAR(255),
    UNIQUE (word, entry_type_id, region_id),
    FOREIGN KEY (source_id) REFERENCES sources(id),
    FOREIGN KEY (entry_type_id) REFERENCES entry_types(id),
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

CREATE TABLE analysis_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_or_url VARCHAR(255) NOT NULL,
    entry_type_id INT NOT NULL,
    region_id INT NOT NULL,
    count INT NOT NULL,
    analyzed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (entry_type_id) REFERENCES entry_types(id),
    FOREIGN KEY (region_id) REFERENCES regions(id)
);