#!/usr/bin/env python3

import string
import os

# TEXT PROCESSING FUNCTION
def clean_text(file_path):
    """Read text, lowercase, remove punctuation, and filter stop words."""
    # Note: Using the original short stop word list to ensure identical output
    stop_words = {'a','an','the','is','in','of','on','and','to','for','at','by'}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()

        # Remove punctuation
        cleaned = text.translate(str.maketrans('', '', string.punctuation))

        # Filter out stop words
        return [word for word in cleaned.split() if word not in stop_words]

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


# WORD SEARCH FUNCTION
def word_search(word, words1, words2):
    """Count how many times the word appears in each essay."""
    count1 = words1.count(word)
    count2 = words2.count(word)
    print(f"\n'{word}' occurs {count1} times in essay1 and {count2} times in essay2.\n")


# COMMON WORDS REPORT
def common_words(words1, words2):
    """Find and print common words between essays."""
    # Using sets for efficient intersection
    common = sorted(set(words1) & set(words2))
    print(f"Common words ({len(common)}):")
    print(", ".join(common) if common else "None found.")
    return common


# PLAGIARISM CALCULATION
def jaccard_similarity(words1, words2):
    """Calculate Jaccard similarity percentage."""
    set1, set2 = set(words1), set(words2)
    if not set1 and not set2:
        return 0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return (intersection / union) * 100

# --- NEW STRUCTURAL FUNCTIONS ---

def load_and_validate_data(files):
    """Loads and cleans the text from the specified file paths."""
    words1 = clean_text(files["essay1"])
    words2 = clean_text(files["essay2"])

    if not words1 or not words2:
        print("Missing or no essay files submitted. Exiting.")
        return None, None
    
    print("\nEssays processed successfully.\n")
    return words1, words2

def run_interactive_search(words1, words2):
    """Handles the user input and execution of the word search feature."""
    # WORD SEARCH (Input is required here to match original output flow)
    search_word = input("Enter a word to search for: ").lower()
    word_search(search_word, words1, words2)

def analyze_and_report_similarity(words1, words2):
    """Calculates common words and similarity, and prints the report."""
    # COMMON WORDS
    commons = common_words(words1, words2)

    # SIMILARITY REPORT
    similarity = jaccard_similarity(words1, words2)
    
    print(f"\nPlagiarism similarity: {similarity:.2f}%")

    # Decision based on threshold
    print(
        "High similarity rate detected (possible plagiarism)."
        if similarity >= 50
        else "Acceptable similarity level detected."
    )
    
    return commons, similarity

def save_report_prompt(commons, similarity):
    """Prompts the user to save the report and handles the file writing."""
    # SAVE REPORT
    save = input("\nSave similarity report? (y/n): ").lower()
    if save == 'y':
        os.makedirs("reports", exist_ok=True)
        report_path = "reports/similarity_report.txt"

        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(f"Similarity: {similarity:.2f}%\n")
                f.write("Common words:\n")
                f.write(", ".join(commons))
            print(f"Report saved to {report_path}")
        except IOError:
            print("Error: Could not save the report file.")

# MAIN PROGRAM (Orchestrator)
def main():
    """Main function to control the application flow."""
    files = {
        "essay1": "essays/essay1.txt",
        "essay2": "essays/essay2.txt"
    }

    # Phase 1: Setup and Validation
    words1, words2 = load_and_validate_data(files)

    if words1 is None or words2 is None:
        return

    # Phase 2: Interactive Word Search
    run_interactive_search(words1, words2)
    
    # Phase 3: Core Analysis and Output
    commons, similarity = analyze_and_report_similarity(words1, words2)

    # Phase 4: Report Saving
    save_report_prompt(commons, similarity)


if __name__ == "__main__":
    main()
