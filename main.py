from collections import Counter


def get_book_contents(path: str) -> str:
    with open(path) as f:
        return f.read()


def book_word_count(book_contents: str) -> int:
    return len(book_contents.split())


def count_characters(book_contents: str) -> dict[str, int]:
    return {**Counter(book_contents.lower())}


def build_report(path_to_book: str) -> str:
    alphas = {
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    }
    nl = "\n"
    contents = get_book_contents(path_to_book)
    word_count = book_word_count(contents)
    char_counts = count_characters(contents)
    # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    main_body = [
        f"The '{k}' character was found {v} times" for k, v in reversed(sorted(char_counts.items(), key=lambda x: x[1])) if k in alphas
    ]
    report_header = f"--- Begin report of {path_to_book} ---"
    report_footer = "--- End report ---"
    return f"""{report_header}
{word_count} words found in the document

{nl.join(main_body)}
{report_footer}
"""


def main() -> None:
    path_to_file = "books/frankenstein.txt"
    print(build_report(path_to_file))


if __name__ == "__main__":
    main()
