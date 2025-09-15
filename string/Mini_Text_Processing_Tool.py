"""
Mini Text Processing Tool
-------------------------
This script reads a multi-line text from the user and performs several
string analyses and transformations.
"""

def count_chars(text: str) -> tuple[int, int]:
    """Return (characters_with_spaces, characters_without_spaces)."""
    return len(text), len(text.replace(" ", ""))

def count_words(text: str) -> int:
    """Return number of words in the text."""
    return len(text.split())

def longest_and_shortest_words(text: str) -> tuple[str, str]:
    """Return the longest and shortest words in the text."""
    words = text.split()
    if not words:
        return "", ""
    longest = max(words, key=len)
    shortest = min(words, key=len)
    return longest, shortest

def count_occurrences(text: str, target: str) -> int:
    """Return how many times a letter or word occurs (case-insensitive)."""
    return text.lower().count(target.lower())

def reverse_each_line(text: str) -> str:
    """Return the text with each line's characters reversed."""
    return "\n".join(line[::-1] for line in text.splitlines())

def to_lowercase(text: str) -> str:
    """Return the entire text in lowercase."""
    return text.lower()

def remove_extra_spaces(text: str) -> str:
    """Remove extra spaces between words."""
    return " ".join(text.split())

def main():
    print("Enter your multi-line text. Press ENTER on a blank line to finish:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    user_text = "\n".join(lines)

    print("\n--- Analysis ---")
    with_spaces, without_spaces = count_chars(user_text)
    print(f"Characters (with spaces): {with_spaces}")
    print(f"Characters (without spaces): {without_spaces}")
    print(f"Word count: {count_words(user_text)}")

    longest, shortest = longest_and_shortest_words(user_text)
    print(f"Longest word: {longest}")
    print(f"Shortest word: {shortest}")

    target = input("\nEnter a letter or word to count: ")
    print(f"Occurrences of '{target}': {count_occurrences(user_text, target)}")

    print("\n--- Transformations ---")
    print("Reversed lines:")
    print(reverse_each_line(user_text))

    print("\nAll lowercase:")
    print(to_lowercase(user_text))

    print("\nWithout extra spaces:")
    print(remove_extra_spaces(user_text))

    # Optional: save to file
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("=== Analysis ===\n")
        f.write(f"Characters (with spaces): {with_spaces}\n")
        f.write(f"Characters (without spaces): {without_spaces}\n")
        f.write(f"Word count: {count_words(user_text)}\n")
        f.write(f"Longest word: {longest}\n")
        f.write(f"Shortest word: {shortest}\n")
        f.write(f"Occurrences of '{target}': {count_occurrences(user_text, target)}\n\n")
        f.write("=== Transformations ===\n")
        f.write("Reversed lines:\n")
        f.write(reverse_each_line(user_text) + "\n\n")
        f.write("All lowercase:\n")
        f.write(to_lowercase(user_text) + "\n\n")
        f.write("Without extra spaces:\n")
        f.write(remove_extra_spaces(user_text) + "\n")

    print("\nA copy of this report has been saved to result.txt")

if __name__ == "__main__":
    main()
