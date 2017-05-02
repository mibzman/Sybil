#print("I got THIS far")
import nltk
#nltk.download('brown')
#nltk.download('punkt')
#from nltk.corpus import brown
from nltk.corpus import wordnet as wn

#print("I got this far")

common_words = ["the", "a", "an", "is", "are", "were", "."]
question_words = ["who", "what", "when", "where", "why", "?"]
pronouns = ["I", "me", "my", "he", "his", "her", "hers", "it", "its", "their", "theirs"]
#text = nltk.Text(word.lower() for word in brown.words())
memory = open("Sybil_memory.txt", "r+")

#find the answer to a question through the data
def get_answer(question):
	tok_q = nltk.word_tokenize(question)
	tag_q = nltk.pos_tag(tok_q)
	line = memory.readline()
	tok_line = nltk.word_tokenize(line)
	tag_line = nltk.pos_tag(tok_line)
	answer  = "I'm sorry, I do not know the answer to that." #default
	while line:
		print("I made it here")
		iterator = 0
		count = 0
		tok_line = nltk.word_tokenize(line)
		tag_line = nltk.pos_tag(tok_line)
		for t in tag_line:
			for q in tag_q:
				if q[0] in question_words:
					continue #do nothing
				elif q[0] in common_words or t[0] in common_words:
					continue #do nothing
				elif q[0] == t[0]: #checks if the words are the same or synonyms
					++count
				count + compare_same(q[0], t[0]) #finds synonyms. returns 1 if it is a synonoym, else 0 so just add this to the count
				print(count)
		if count >= 3:
			answer = line
			break
		++iterator
		line = memory.readline(iterator)
	print(answer) #output(answer) #testing purposes

#finds synonyms
def compare_same(word_memory, word_question):
	if word_memory in wn.synsets(word_question):
		return 1
	else:
		return 0
		


#question or data?
def determine_input(data):
	print("I got thiiiiiiiis far")
	new_data = nltk.word_tokenize(data)
	if new_data[0] in question_words:
		get_answer(data)
	else:
		memory.write(data)	

#gives the answer in a reasonable format
#example: if the data was "I met with my teacher" the output would be "met teacher"
def output(answer):
	tok_answer = nltk.word_tokenize(answer)
	tag_answer = nltk.pos_tag(tok_answer)
	noun = " "
	verb = " "
	for t in tag_answer:
		if t[1] == "NN":
			if t[0] not in pronouns:
				noun = t[0]
		elif t[1] == "VB":
			verb = t[0]
	print(verb + " " + noun)

#testing purposes
print("Hello, carbon based lifeform. I am Sybil, your personal Librarian. Please add data to my library, then I can recall what you've told me.")
user_in = 0
while user_in != 1:
	data = raw_input("Tell me something!")
	determine_input(data)
	user_in = raw_input("Enter 1 to quit or anything else to continue.")





