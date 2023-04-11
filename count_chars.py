from json import dump
import requests


URL = 'https://www.python.org/'

def main():
	page_text = requests.get(URL).text
	list_of_chars = list(page_text)
	unique_chars = set(list_of_chars)
	output = dict()
	for character in unique_chars:
		output[character] = list_of_chars.count(character)
	with open('readme.md', 'w') as file:
		dump(output, file, indent=4)



if __name__ == '__main__':
	main()