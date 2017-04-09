import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import codecs
class_1_dic = {}
class_2_dic = {}
allwords = {}
total_sample = 0
class_1_sample = 0
class_2_sample = 0
class_1_size = 0
class_2_size = 0
def addOne(word):
	global class_1_size
	global class_2_size
	if word in class_1_dic:
		class_1_dic[word] += 1
	else:
		class_1_dic[word] = 1
	class_1_size += class_1_dic[word]
	if word in class_2_dic:
		class_2_dic[word] += 1
	else:
		class_2_dic[word] = 1
	class_2_size += class_2_dic[word]
def calculate(dictionary, size):
	for word in dictionary:
		count = dictionary[word]
		dictionary[word] = float(count)/float(size)
def process():
	global class_1_size
	global class_2_size
	for word in allwords:
		addOne(word)
	calculate(class_1_dic, class_1_size)
	calculate(class_2_dic, class_2_size)
def addToDic(dictionary, word_list):
	for word in word_list:
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1
class_1_file = list(codecs.open('data/pos_train.txt', "r", "utf-8").readlines())
#with open('data/pos_train.txt', 'r') as class_1_file:
for line in class_1_file:
	total_sample += 1
	line = line.strip()
	word_list = line.split(" ")

	addToDic(class_1_dic, word_list)
	addToDic(allwords, word_list)
	class_1_sample += 1
	#class_1_file.close()
class_2_file = list(codecs.open('data/neg_train.txt', "r", "utf-8").readlines())
#with open('data/neg_train.txt', 'r') as class_2_file:
for line in class_2_file:
	total_sample += 1
	line = line.strip()
	word_list = line.split(" ")
	addToDic(class_2_dic, word_list)
	addToDic(allwords, word_list)
	class_2_sample += 1
	#class_2_file.close()
prior_class_1 = float(class_1_sample)/float(total_sample)
prior_class_2 = float(class_1_sample)/float(total_sample)
process()
with open("my_nb_model.txt",'w') as model:
	model.write(str(prior_class_1)+'\n')
	model.write(str(prior_class_2)+'\n')
	for word in allwords:
		model.write(word+'\n')
		model.write(str(class_1_dic[word])+'\n')
		model.write(str(class_2_dic[word])+'\n')
	model.close()
