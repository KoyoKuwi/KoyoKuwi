#The MIT License (MIT)

# Copyright (c) 2016 KoyoKuwi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import math
import string
import sys

def read_txt(filename):
	"""
	Read the text file and make sure it is a plain text file
	with .txt extension;
	Return a list of the lines of text in the text file.
	"""
	try:
		if filename.endswith('.txt'):
			with open(filename, 'r') as txt:
				text = txt.read()
				return text
		else:
			print("Invalid File")
			sys.exit(1) 
	except:
		print(sys.exc_info())
		sys.exit(1)        
        
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,\
                                  " "*len(string.punctuation)+string.ascii_lowercase)
def normalize_text(text):
	"""
	Fake stemmer;
	Return text after normalization.
	"""
	text = text.translate(translation_table)
	return text

def tokenize_text(text):
	"""
	Fake tokenizer;
	Return a list of words
	"""
	return text.split()

def word_freq(words):
	"""
	Return dictionary
	"""
	index = {}
	for word in words:
		if word in index:
			index[word] += 1
		else:
			index[word] = 1
	return index

def doc_freq(filename):
	"""
	Count the frequency
	Return key-value pairs of word and frequency
	"""
	text = read_txt(filename)
	text = normalize_text(text)
	words = tokenize_text(text)
	freq = word_freq(words)
	return freq

def inner_product(koyo, kuwi):
	"""
	Inner product between koyo kuwi.
	"""
	inner = sum(koyo[key] * kuwi.get(key, 0.0) for key in koyo) 
	return inner

def vector_angle(koyo, kuwi):
	"""
	Calculate the vector angle of koyo kuwi.
	Return the angle of koyo kuwi
	"""
	nur = inner_product(koyo, kuwi)
	den = math.sqrt(inner_product(koyo, koyo)*inner_product(kuwi, kuwi))
	return math.acos(nur/den)

def percentage(koyo, kuwi):
	"""
	Calculate koyo kuwi score
	Return percentage of similarity
	"""
	half = math.pi / 2
	angle = vector_angle(koyo, kuwi)
	percentage = (half - angle) / half * 100
	return percentage

def score(koyo, kuwi):
	"""
	Get the similarity score
	Return the score as percentage 
	"""
	freq_koyo = doc_freq(koyo)
	freq_kuwi = doc_freq(kuwi)
	koyokuwi = percentage(freq_koyo, freq_kuwi)
	return koyokuwi