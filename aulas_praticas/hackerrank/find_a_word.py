import re
import sys

# Word -> sequence of characteres -> lowercase, uppercase, digits and underscore.
# Word -> \w

# Input
# -> Sentences
# -> Words to count in the sentences

words = {}

word_expr = r'\b\w+\b'

# Counts the words in the sentences
for _ in range(int(next(sys.stdin))):
    line = next(sys.stdin)
    found_words = re.findall(word_expr, line)
    for w in found_words:
        if not w in words:
            words[w] = 1
        else:
            words[w] += 1

# Note: Given the input's size, this method is fine
# But if the input was to be a much bigger one,
# there was no need to count the number of the words that we do need to know

# Prints the occurrences of the given words in the sentences
for _ in range(int(next(sys.stdin))):
    word = next(sys.stdin).strip()
    print(words[word])
