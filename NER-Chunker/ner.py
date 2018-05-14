import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from app_index import sentence

nltk.download('maxent_ne_chunker')
nltk.download('words')

if __name__ == "__main__":
    
	tokens = nltk.word_tokenize(sentence)
	print("tokens = %s" % tokens)

	tagged = nltk.pos_tag(tokens)

	entities = nltk.chunk.ne_chunk(tagged)
	print("entities = %s" % entities)
