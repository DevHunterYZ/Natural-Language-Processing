import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
train_text = state_union.raw("C:/Users/user/Desktop/2017Balkon.txt")
sample_text = state_union.raw("C:/Users/user/Desktop/2018Balkon.txt")
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
