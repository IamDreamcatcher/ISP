import functions
import constants


def main():
    text = functions.get_text(constants.FIlE_NAME)
    n, k = functions.get_params()

    words = functions.get_words(text)
    dict_of_word = functions.get_dict_of_words(words)
    median_value, average_value = functions.get_sentences_statistics(text)
    ngrams = functions.find_top_ngrams(dict_of_word, n, k)

    functions.print_data(dict_of_word, ngrams, median_value, average_value)


if __name__ == "__main__":
    main()
