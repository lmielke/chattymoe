# general.py

def insert_newline(text, maxLen=5, *args, **kwargs):
    """
    inserts a newline after every maxLen words
    Example: If a text is longer than n words, it will be split into n / maxLen lines.
    """
    numWords = len(text.split())
    if numWords <= maxLen:
        return [text]
    else:
        newText, line = [], ''
        for i, word in enumerate(text.split(), 1):
            line += f"{word} "
            if i % maxLen == 0 and i != 0:
                # print('\t', line)
                newText.append(line)
                line = ''
        return newText