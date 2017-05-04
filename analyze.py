from __future__ import print_function #
import nltk
import string
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet as wn

common_words = ["the", "a", "an", "is", "are", "were", "."]
question_words = ["who", "what", "when", "where", "why", "?"]
pronouns = ["I", "me", "my", "he", "his", "her", "hers", "it", "its", "their", "theirs"]
#text = nltk.Text(word.lower() for word in brown.words())
memory = open("Sybil_memory.txt", "r+")

#find the answer to a question through the data
def get_answer(question):
	question = question.translate(None, string.punctuation)
	questionArr = question.split()
	# line = memory.readline()

	# answerLineArr = line.split()
	# what do i really hope works like its supposed to?
	answer  = "I'm sorry, I do not know the answer to that." #default

	with open("Sybil_memory.txt", "r+") as memory:
		for line in memory:
			answerLineArr = line.split()
			count = 0
			for t in answerLineArr:
				for q in questionArr:
					if q.lower() in question_words:
						continue #do nothing
					elif q.lower() in common_words or t in common_words:
						continue #do nothing
					elif q.lower() == t.lower() or are_synonyms(q, t): #checks if the words are the same or synonyms
						count += 1
					# print(count, q, t)
			if count >= 3:
				# print(line)
				return line
				# answer = line
				# break
		# print("line:", line)

	return answer #output(answer) #testing purposes

#find the answer to a question through the data
def are_synonyms(first, second):
	# print(first)
	# print(second)
	# print(wn.synsets(second).lemma_names)

	for index, meaning in enumerate(wn.synsets(first)):
	  for word in meaning.lemma_names():
	  	if word == second:
	  		return True

	return False

#question or data?
def analyze(data):
	new_data = nltk.word_tokenize(data)
	if "?" in new_data or new_data[0] in question_words:
		return get_answer(data)
	else:
		with open("Sybil_memory.txt", "a") as f:
			f.write(data + "\n")
		# with open("Sybil_memory.txt", "a") as myfile:
    		# myfile.write(data)	
		return "Thanks, I'll remember that!"

#gives the answer in a reasonable format
#example: if the data was "I met with my teacher" the output would be "met teacher"
def output(answer):
	tok_answer = nltk.word_tokenize(answer)
	tag_answer = nltk.pos_tag(tok_answer)
	noun = " "
	verb = " "
	for t in tag_answer:
		# prev_word = t - 1
		if t[1] == "NN":
			if t[0] not in pronouns:
				noun = t[0]
		elif t[1] == "VB":
			verb = t[0]
	print(verb + " " + noun)

def Testing():
	print("Hello, carbon based lifeform. I am Sybil, your personal Librarian. Please add data to my library, then I can recall what you've told me.")
	user_in = 0
	while user_in != 1:
		data = raw_input("Tell me something!")
		print(analyze(data))

Testing()