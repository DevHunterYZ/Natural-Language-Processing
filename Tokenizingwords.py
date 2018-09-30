import nltk
nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Merhaba dostum, bugün nasılsın? Hava güzel, ama Python daha da güzel. Kilo vermek istiyorsan tatlı yememelisin."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))
