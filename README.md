# Comparing and Analyzing the Word-Level and Phoneme Overlap of Amharic and Tigrigna

## 📄 Abstract

This project explores the linguistic similarities between Amharic and Tigrigna by analyzing word-level and phoneme overlap between the two languages. Utilizing a combination of Python programming and phoneme conversion tools, the study quantifies the degree of overlap, providing insights into the structural and phonetic relationships between these closely related Semitic languages. The results reveal significant phonetic similarities and notable word-level overlap, contributing to the understanding of the linguistic proximity between Amharic and Tigrigna.

## 🔍 Introduction

Amharic and Tigrigna are both members of the Semitic branch of the Afro-Asiatic language family, spoken predominantly in Ethiopia and Eritrea. Despite their shared linguistic heritage, they exhibit distinct phonetic, lexical, and syntactic characteristics.  
This project aims to quantify the degree of similarity between Amharic and Tigrigna by comparing word-level and phoneme overlaps. By leveraging phoneme conversion algorithms and analyzing the resulting data, the study provides a clearer picture of the linguistic relationship between the two languages.

---

## 🧪 Methodology

The methodology for comparing and analyzing the word-level and phoneme overlap involved several stages, all implemented in Python.

### 1. Data Preprocessing
- Cleaned the text data by removing punctuation and non-phonetic characters using `clear_non_alphabet`.
- Stored the cleaned text in a standardized format for further processing.

### 2. Phoneme Conversion
- Applied a SERA-based grapheme-to-phoneme algorithm using `convert_to_phonemes`.
- Stored phonetic representations for further phoneme-level analysis.

### 3. Word-Level Comparison
- Used `frequency_counter` to analyze word frequency in both languages.
- Computed:
Similarity Percentage = (Number of Common Words) / (Total Unique Words - Common Words) × 100
- Saved results including word counts and similarity percentage.

### 4. Phoneme-Level Comparison
- Counted phoneme frequency using `phoneme_frequency_counter`.
- Applied the same similarity formula for phonemes.
- Stored phoneme similarity data.

### 5. Reporting & Output
- Generated a summary of word and phoneme overlaps.
- Informed the user where all generated files (cleaned text, phoneme text, result files) were saved.

---

## 📊 Results and Discussion

### 📌 Word-Level Overlap
- Test 1: 498 Amharic vs 569 Tigrigna → 27 common words → 4.05% overlap
- Test 2: 706 Amharic vs 793 Tigrigna → 18 common words → 1.77% overlap
- Test 3: 12,634 Amharic vs 14,567 Tigrigna → 180 common words → 1.84% overlap

These results suggest low lexical overlap between the languages.

### 🔠 Phoneme-Level Overlap
- Test 1: 97.14%
- Test 2: 94.29%
- Test 3: 94.44%

This shows a strong similarity in phonetic structure, consistent with their common Semitic roots.

### 🧠 Discussion
- Low word-level overlap reflects distinct vocabularies.
- High phoneme overlap indicates shared phonetic structure.
- Implications:
1. Confirms linguistic divergence despite common ancestry.
2. Supports NLP applications like speech recognition and translation.
3. Aids language learners by showing shared pronunciation patterns.

---

## ✅ Conclusion

This study provides a detailed comparison of Amharic and Tigrigna, showing:
- Low lexical overlap
- High phonetic overlap

These results offer valuable insight into the relationship between the two languages and open up future directions in language technology and education. Further analysis of syntax and morphology could deepen this understanding.

---

## 📁 Project Structure
├── data/
│ ├── raw_text/
│ ├── cleaned_text/
│ └── phoneme_text/
├── results/
│ ├── word_overlap.txt
│ └── phoneme_overlap.txt
├── src/
│ └── main.py
└── README.txt

## ⚙️ Technologies Used
- Python 3.x
- Regular Expressions
- SERA-based G2P conversion
- File I/O and text processing

## 📚 References
1. https://www.geeksforgeeks.org/text-preprocessing-in-python-set-1/
2. https://github.com/berknology/text-preprocessing
3. https://en.wikipedia.org/wiki/Help:IPA/Amharic
4. https://en.wikipedia.org/wiki/Help:IPA/Tigriyna
5. https://bible.geezexperience.com
