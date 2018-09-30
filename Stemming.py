from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
example_words = ["make","making","maked","makely","maker"]
for w in example_words:
    print(ps.stem(w))
new_text = "It is important to by very makely while you are making with make. All makers have maked poorly at least once."
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
