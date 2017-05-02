from __future__ import print_function #
import nltk
import string
#nltk.download('brown')
nltk.download('punkt')
#from nltk.corpus import brown

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
					elif q.lower() == t.lower(): #checks if the words are the same or synonyms
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
	# tok_q = nltk.word_tokenize(question)
	# tag_q = nltk.pos_tag(tok_q)
	# line = memory.readline()
	# tok_line = nltk.word_tokenize(line)
	# tag_line = nltk.pos_tag(tok_line)
	# answer  = "I'm sorry, I do not know the answer to that." #default
	# while line:
	# 	iterator = 0
	# 	count = 0
	# 	tok_line = nltk.word_tokenize(line)
	# 	tag_line = nltk.pos_tag(tok_line)
	# 	for t in tag_line:
	# 		for q in tag_q:
	# 			if q[0] in question_words:
	# 				continue #do nothing
	# 			elif q[0] in common_words or t[0] in common_words:
	# 				continue #do nothing
	# 			elif q[0] == t[0]: #checks if the words are the same or synonyms
	# 				++count
	# 	if count >= 3:
	# 		answer = line
	# 		break
	# 	++iterator
	# 	line = memory.readline(iterator)
	# print(answer) #output(answer) #testing purposes
	return false

#question or data?
def analyze(data):
	new_data = nltk.word_tokenize(data)
	if "?" in new_data or new_data[0] in question_words:
		return get_answer(data)
	else:
		memory.write(data)	
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

#testing purposes
print("Hello, carbon based lifeform. I am Sybil, your personal Librarian. Please add data to my library, then I can recall what you've told me.")
user_in = 0
while user_in != 1:
	data = raw_input("Tell me something!")
	print(analyze(data))
	# user_in = raw_input("Enter 1 to quit or anything else to continue.")

#test