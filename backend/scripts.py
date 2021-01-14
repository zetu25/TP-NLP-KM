# import spacy
import spacy
import numpy
nlp = spacy.load('fr_core_news_lg')

def return_word_vector(word):
    return numpy.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]])
    
def return_most_n_similar(word,n=5):
    most_similar = nlp.vocab.vectors.most_similar(return_word_vector(word),n=n)
    return [nlp.vocab.strings[w] for w in most_similar[0][0]]

def print_similar_word(list_of_similar):
    [print(word) for word in list_of_similar]


if __name__ == '__main__':
    print(return_most_n_similar("Apple",20))

    
    


