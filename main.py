import re
import os
from collections import Counter
import sera_mapper_v1


def clear_non_alphabet(text):
    """Cleans non-Amharic alphabetic characters from the text."""
    pattern = r'[^\u1200-\u135A\s]'
    return re.sub(pattern, '', text)


def clean_text(input_file, output_directory='cleaned_text'):
    """Cleans a single text file and saves it to the output directory."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = clear_non_alphabet(text)
    output_file = os.path.join(output_directory, "cleaned_" + os.path.basename(input_file))

    with open(output_file, 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write(cleaned_text)

    return cleaned_text


def convert_to_phonemes(text):
    return sera_mapper_v1.convert_string(text, sera_mapper_v1.to_dic())


def phoneme_txt(file1, file2, output_directory='text_in_phoneme'):
    """Converts text to phonemes and saves to files."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    amharic_phonemes = convert_to_phonemes(clean_text(file1))
    tigrigna_phonemes = convert_to_phonemes(clean_text(file2))

    with open(os.path.join(output_directory, "phonemes_" + os.path.basename(file1)), 'w', encoding='utf-8') as file:
        file.write(amharic_phonemes)

    with open(os.path.join(output_directory, "phonemes_" + os.path.basename(file2)), 'w', encoding='utf-8') as file:
        file.write(tigrigna_phonemes)


def frequency_counter(text):
    return Counter(text.split())


def word_level_comparison(file1, file2):
    amharic_processed = clean_text(file1)
    tigrigna_processed = clean_text(file2)

    amharic_word_freq = frequency_counter(amharic_processed)
    tigrigna_word_freq = frequency_counter(tigrigna_processed)

    amharic_words = set(amharic_word_freq.keys())
    tigrigna_words = set(tigrigna_word_freq.keys())
    common_words = amharic_words.intersection(tigrigna_words)
    print(f"Total number of shared words = {len(common_words)}")
    try:
        similarity_percentage = (len(common_words) /
                                 (len(amharic_words) + len(tigrigna_words) - len(common_words))) * 100
        similarity_percentage = round(similarity_percentage, 2)

        result_file = "word_level_comparison_result.txt"
        with open(result_file, "w", encoding="utf-8") as f:
            f.write("Word-Level Comparison\n")
            f.write("------------------------\n")
            f.write(f"Total words in {file1}: {len(amharic_processed.split())}\n")
            f.write(f"Total words in {file2}: {len(tigrigna_processed.split())}\n")
            f.write(f"Unique words in {file1}: {len(amharic_words)}\n")
            f.write(f"Unique words in {file2}: {len(tigrigna_words)}\n")
            f.write(f"Number of common words: {len(common_words)}\n")
            f.write("Common words:\n")
            f.write(f"{common_words}\n")
            f.write(f"Word-level similarity: {similarity_percentage}%")

        return similarity_percentage
    except ZeroDivisionError:
        print("Zero division error: Check if the files have written text!")


def phoneme_level_comparison(file1, file2):
    def phoneme_frequency_counter(text):
        phonemes = convert_to_phonemes(text)
        return Counter(phonemes)

    amharic_phoneme_freq = phoneme_frequency_counter(clean_text(file1))
    tigrigna_phoneme_freq = phoneme_frequency_counter(clean_text(file2))

    amharic_phoneme_characters = set(amharic_phoneme_freq.keys())
    tigrigna_phoneme_characters = set(tigrigna_phoneme_freq.keys())
    common_phonemes_characters = amharic_phoneme_characters.intersection(tigrigna_phoneme_characters)

    try:
        similarity_percentage = (len(common_phonemes_characters) /
                                 (len(amharic_phoneme_characters) + len(tigrigna_phoneme_characters) - len(
                                     common_phonemes_characters))) * 100
        similarity_percentage = round(similarity_percentage, 2)

        result_file = "phoneme_level_comparison_result.txt"
        with open(result_file, "w", encoding="utf-8") as f:
            f.write("Phoneme-Level Comparison\n")
            f.write("------------------------\n")
            f.write(f"Total phonemes in {file1}: {len(amharic_phoneme_characters)}\n")
            f.write(f"Total phonemes in {file2}: {len(tigrigna_phoneme_characters)}\n")
            f.write(f"Number of common phonemes: {len(common_phonemes_characters)}\n")
            f.write(f"Phoneme-level similarity: {similarity_percentage}%")

        return similarity_percentage
    except ZeroDivisionError:
        print("Zero division error: Check if the files have written text!")


amharic_file = "amharic1.txt"
tigrigna_file = "tigrigna1.txt"

phoneme_txt(amharic_file, tigrigna_file)
word_similarity = word_level_comparison(amharic_file, tigrigna_file)
phoneme_similarity = phoneme_level_comparison(amharic_file, tigrigna_file)
message = """The pre-processed text file, The grapheme to phoneme converted text file also the reports of the both
word level and phoneme level comparison are found in the main directory!"""

print(f"Total words in {amharic_file}: {len(clean_text(amharic_file).split())}")
print(f"Total words in {tigrigna_file}: {len(clean_text(tigrigna_file).split())}")
print(f"Percentage word level overlap: {word_similarity}%")
print(f"Percentage phoneme level overlap: {phoneme_similarity}%")
print()
print(message)
