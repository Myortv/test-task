import json

import datetime


def main():
	fp = input('Input filepath: ')
	new_file = str()
	with open(fp, 'r') as file:
		data = json.load(file)
	for key, item in data.items():
		if item == 'updated' or key == 'updated':
			data[key] = datetime.datetime.now().isoformat()
	with open(fp, 'w') as file:
		json.dump(data, file)


if __name__ == '__main__':
	main()
