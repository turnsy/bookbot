def count_words(content: str) -> int:
    return len(content.split())

def count_characters(content: str):
    counts = {}
    alphabet = set([c for c in "abcdefghijklmnopqrstuvwxyz"])
    for c in content:
        c_lower = c.lower()

        if c_lower not in alphabet:
            continue

        if c_lower not in counts:
            counts[c_lower] = 1
        else:
            counts[c_lower] += 1
    
    return counts

def build_report(path: str, char_counts: dict, word_count: int):
    res = [f"--- Begin report of {path} ---"]
    res.append(f"{word_count} words found in the document")
    res.append("\n")
    for char, count in char_counts.items():
        res.append(f"The '{char}' character was found {count} times")

    return res

if __name__ == "__main__":
    path = "books/frankenstein.txt"

    with open(path) as f:
        content = f.read()
        report = build_report(path, count_characters(content), count_words(content))

        for line in report:
            print(line)
