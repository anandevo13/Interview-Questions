"""
Q. Put spaces between words starting with capital letters
"""

# Function to amend the sentence
def amendSentence(string):
	string = list(string)

	# Traverse the string
	for i in range(len(string)):

		# Convert to lowercase if its
		# an uppercase character
		if string[i] >= 'A' and string[i] <= 'Z':
			string[i] = chr(ord(string[i]) + 32)

			# Print space before it
			# if its an uppercase character
			if i != 0:
				print(" ", end = "")

			# Print the character
			print(string[i], end = "")

		# if lowercase character
		# then just print
		else:
			print(string[i], end = "")

# Driver Code
if __name__ == "__main__":
	string = "BruceWayneIsBatman"
	amendSentence(string)

# Another method : Using Regex

import re
 
def putSpace(input):
 
    # regex [A-Z][a-z]* means any string starting
    # with capital character followed by many
    # lowercase letters
    words = re.findall('[A-Z][a-z]*', input)
 
    # Change first letter of each word into lower
    # case
    for i in range(0, len(words)):
        words[i] = words[i][0].lower()+words[i][1:]
    print(' '.join(words))
 
 
# Driver program
if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    putSpace(input)
    

# Another method:

import re
#input
string='HelloWorldOfPython'
#Find the words in string starting with uppercase letter. 
words = re.findall('[A-Z][a-z]*', string)
#concatenate the word with space
print(' '.join((words)))


# Another method:
 
import re
#input
string='LetUsStudyPython'
#Find the words in string starting with uppercase letter. 
words = re.findall('[A-Z][a-z]*', string)
#concatenate the word with space
print(' '.join((words)))   

