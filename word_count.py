# ============================================================
#  Day 1 Mini Project — Word Count Script
#  For: .NET / C# developer learning Python for GenAI
# ============================================================
#
#  HOW TO RUN:
#    python word_count.py                  <- counts sample text
#    python word_count.py myfile.txt       <- counts your file
#
# ============================================================

import sys
import os
from collections import Counter


# ------------------------------------------------------------
# C# equivalent:
#   public record CountResult(int Lines, int Words, ...)
# ------------------------------------------------------------
def count_text(text: str) -> dict:
    """Count lines, words, characters and unique words in text."""

    lines       = text.splitlines()
    words       = text.split()
    chars_total = len(text)
    chars_no_sp = len(text.replace(" ", "").replace("\n", ""))

    # unique words — case insensitive
    # C# equivalent: words.Select(w => w.ToLower()).Distinct().Count()
    unique_words = set(w.lower().strip(".,!?;:\"'") for w in words)

    # top 5 most frequent words (bonus — like LINQ GroupBy + OrderBy)
    word_freq = Counter(w.lower().strip(".,!?;:\"'") for w in words)
    top_words = word_freq.most_common(5)

    return {
        "lines"       : len(lines),
        "words"       : len(words),
        "chars_total" : chars_total,
        "chars_no_sp" : chars_no_sp,
        "unique_words": len(unique_words),
        "top_words"   : top_words,
    }


# ------------------------------------------------------------
# C# equivalent:
#   public void PrintResults(CountResult result, string source)
# ------------------------------------------------------------
def print_results(result: dict, source: str) -> None:
    """Print the word count results in a readable format."""

    print()
    print("=" * 50)
    print(f"  Results for: {source}")
    print("=" * 50)
    print(f"  Lines         : {result['lines']}")
    print(f"  Words         : {result['words']}")
    print(f"  Characters    : {result['chars_total']}  (no spaces: {result['chars_no_sp']})")
    print(f"  Unique words  : {result['unique_words']}")
    print()
    print("  Top 5 words:")
    for word, count in result["top_words"]:
        bar = "#" * count
        print(f"    {word:<15} {count:>3}  {bar}")
    print("=" * 50)
    print()


# ------------------------------------------------------------
# C# equivalent:  static void Main(string[] args)
# ------------------------------------------------------------
def main() -> None:

    if len(sys.argv) > 1:
        filepath = sys.argv[1]

        if not os.path.exists(filepath):
            print(f"Error: file '{filepath}' not found.")
            sys.exit(1)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        result = count_text(text)
        print_results(result, source=filepath)

    else:
        sample = """
        Python is a high-level, general-purpose programming language.
        Its design philosophy emphasizes code readability with the use
        of significant indentation. Python is dynamically typed and
        garbage-collected. It supports multiple programming paradigms,
        including structured, object-oriented and functional programming.

        Python is often described as a batteries included language due
        to its comprehensive standard library. It is used in web
        development, data science, artificial intelligence, and more.
        Many developers love Python for its clean and readable syntax.
        """

        result = count_text(sample)
        print_results(result, source="sample text (built-in)")
        print("  Tip: run with your own file:")
        print("       python word_count.py yourfile.txt")
        print()


# Only runs when executed directly, not when imported
if __name__ == "__main__":
    main()
