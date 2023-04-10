import logging
from sys import byteorder
# logging.getLogger().setLevel(logging.INFO)


def swap_bytes(number: int) -> int:
	number = bytearray(
		number.to_bytes(2, byteorder)
	)
	output = bytearray()
	output.append(number[1])
	output.append(number[0])
	return int.from_bytes(output, byteorder)


def validate_input(input: str) -> int:
	try:
		input = int(input)
		if input.bit_length() > 16:
			raise ValueError
		return input
	except ValueError as e:
		logging.info(
			'Value error occured, is input value is legit int?'
		)


def main():
	input_number = None
	while not input_number:
		input_number = validate_input(
			input('Input 2 byte int: ')
		)
	swapped_number = swap_bytes(input_number)
	print(f'result of bytes swapping:\n\t{swapped_number}')

if __name__ == '__main__':
	main()