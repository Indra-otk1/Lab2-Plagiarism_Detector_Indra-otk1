import string
import os

# TEXT PROCESSING FUNCTION
def clean_text(file_path):
    """Read text, lowercase, remove punctuation, and filter stop words."""
    stop_words = {'a','an','the','is','in','of','on','and','to','for','at','by'}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower()
        # remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = [w for w in text.split() if w not in stop_words]
        return words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

# WORD SEARCH FUNCTION
def word_search(word, words1, words2):
    """Count how many times words appears in each of the essay."""
    count1 = words1.count(word)
    count2 = words2.count(word)
    print(f"\n'{word}' occurs {count1} times in essay1 and {count2} times in essay2.\n")

# COMMON WORDS REPORT
def common_words(words1, words2):
    """Returns and print the common words that appear between between essays."""
    common = set(words1) & set(words2)
    print(f"Common words ({len(common)}):")
    print(", ".join(sorted(common)) if common else "None found.")
    return common

# PLAGIARISM CALCULATION
def jaccard_similarity(words1, words2):
    """Calculate Jaccard similarity percentage."""
    set1, set2 = set(words1), set(words2)
    intersection = set1 & set2
    union = set1 | set2
    return (len(intersection) / len(union)) * 100 if union else 0

# MAIN PROGRAM
def main():
    essay1 = "essays/essay1.txt"
    essay2 = "essays/essay2.txt"

    words1 = clean_text(essay1)
    words2 = clean_text(essay2)

    if not words1 or not words2:
        print("Missing or no  essay filessubmitted. Exiting.")
        return

    print("\n Essays processed successfully.\n")

    # Word search
    word = input("Enter a word to search for: ").lower()
    word_search(word, words1, words2)

    # Common words
    common = common_words(words1, words2)

    # Similarity calculation
    plagiarism_percent = jaccard_similarity(words1, words2)
    print(f"\nPlagiarism similarity: {plagiarism_percent:.2f}%")

    if plagiarism_percent >= 50:
        print("High similarity rate  detected (possible plagiarism).")
    else:
        print("Acceptable similarity level detected.")

    # Option to save report
    choice = input("\nSave similarity report? (y/n): ").lower()
    if choice == 'y':
        os.makedirs('reports', exist_ok=True)
        report_path = "reports/similarity_report.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"Similarity: {plagiarism_percent:.2f}%\n")
            f.write("Common words:\n")
            f.write(", ".join(sorted(common)))
        print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
