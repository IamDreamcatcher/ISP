from fileinput import filename
import re
import constants
from collections import defaultdict
from collections import Counter
from typing import List, Tuple, Dict


def get_text(filename: str) -> str:
    with open(filename, "r") as file:
        text = file.read()

    return text


def get_words(text: str) -> List[str]:
    words: List[str] = []

    splitted_words = text.split()
    for word in splitted_words:
        words.append(word.strip(constants.PUNCTUATION_MARKS).lower())

    return [x for x in words if len(x) > 0]


def get_word_amount(text: str) -> List[int]:
    words_amount: List[int] = []

    sentences = re.split(constants.REGEX_FOR_SENTENCE, text)
    for sentence in sentences:
        words_amount.append(len(get_words(sentence)))

    return words_amount


def get_dict_of_words(text: List[str]) -> Dict[str, int]:
    dict_of_words: Dict[str, int] = Counter(text)

    return dict_of_words


def find_top_ngrams(dict_of_words: Dict[str, int], n: int, k: int) -> List[Tuple[str, int]]:
    ngrams: Dict[str, int] = defaultdict(int)
    for word, value in dict_of_words.items():
        for left_position in range(0, len(word) - n + 1):
            ngrams[word[left_position: left_position + n]] += value

    top_ngrams = sorted(ngrams.items(), key=lambda item: item[1])
    top_ngrams.reverse()
    top_ngrams = top_ngrams[:k]

    return top_ngrams


def print_data(dict_of_word: Dict[str, int], ngrams: List[Tuple[str, int]],
               median_value: float, average_value: float):
    print("Dictionary of words:")
    for word, word_number in dict_of_word.items():
        print(f"{word}: {word_number}")

    print("Top k ngrams:")
    for word, word_number in ngrams:
        print(f"{word}: {word_number}")

    print(f"Median value of words in sentence: {median_value}")
    print(f"Average value of words in sentence: {average_value}")


def get_params() -> Tuple[int, int]:
    buffer: str = input("Enter N\n")
    if buffer.isdigit():
        n = int(buffer)
    else:
        n = constants.CONST_N

    buffer = input("Enter K\n")
    if buffer.isdigit():
        k = int(buffer)
    else:
        k = constants.CONST_K

    return n, k
