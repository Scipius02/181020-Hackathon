"""  Clicking (input) increases score. Over time, will lower gradually. 
	 
"""
# Translate message returns translated string, single word
import time

# Sample: create dictionary for which each key is a separate word from the translated string
# Each value is the corresponding global_mastery val
global_mastery = {}
'''
message = "This is a sample sentence to demonstrate dictionary effectiveness."

for word in message.split():
	global_mastery.update({word: 0})
	
print global_mastery'''

#add new word from clicked input HERE *******
new_word = "hello"
global_mastery[new_word] = 1  
'''for value, key in global_mastery.items():
	global_mastery[value] += 5'''

print global_mastery

# only add parsed words into the dictionary
# global_mastery.update({word, 0})

start = time.time()

# timer that decrements global_mastery over time until it is reset to 0
red = 3
orange = 2
yellow = 1

while True:
	elapsed = (time.time() - start)
	if elapsed % 5 == 0:
		for value, key in global_mastery.items():
			if global_mastery[value] != 0:
				global_mastery[value] -= 1
		print elapsed
		print global_mastery
	#if click happens
	
