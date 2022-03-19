import functions
import constants
import statistics

def main():
    text = functions.get_text(constants.FILE_NAME)
    n, k = functions.get_params()

    words = functions.get_words(text)
    dict_of_word = functions.get_dict_of_words(words)
    words_amount = get_word_amount(text)
    median_value = statistics.median(words_amount)
    average_value = statistics.fmean(words_amount)
    ngrams = functions.find_top_ngrams(dict_of_word, n, k)

    functions.print_data(dict_of_word, ngrams, median_value, average_value)


if __name__ == "__main__":
    main()
