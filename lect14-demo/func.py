def swap_words(sentence):
    words = sentence.split()
    if len(words) == 1:
        return words[0]
    return " ".join([words[-1]] + words[1:-1] + [words[0]])
