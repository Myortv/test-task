from typing import Tuple
import logging


logging.getLogger().setLevel(logging.INFO)


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


def input_(banner: str):
	input_number = None
	while not input_number:
		input_number = validate_input(
			input(banner)
		)
	return input_number


def read_input() -> Tuple[int]:
	buskets_amount = input_(
		'Input amount of buskets (N): '
	)
	coin_weight = input_(
		'Input coin weight (w): '
	)
	coin_difference = input_(
		'Input fake coin differenve (d): '
	)
	faked_mass = input_(
		'Input total weight of picked coins (N): '
	)
	output = (
		buskets_amount, 
		coin_weight,
		coin_difference,
		faked_mass,
	)
	return output


def calculate_answer(values: Tuple[int]):
	"""
		I could add other layer, create functions for every
		calculation step and add validation as some sort of dependency
		or decorator, but it make all even worse -- bunch of functions
		that make only one calculation and not enought verbouse names of them
		make it super hard to debug. It understandable that in products i'll
		get more complicated funcions and some sort of validations
		will apply to them but in that case it's better leave all like that imo
	"""
	buskets, weight, coin_difference, mass = values
	active_busket = buskets - 1
	if coin_difference <= weight:
		raise ValueError('Coin different is bigger than coin weight')
	if active_busket < 1:
		raise ValueError('Active busket lower than one')
	coins_picked = active_busket * 0.5 * (active_busket + 1)
	difference = (coins_picked * weight) - mass
	if difference == 0:
		return buskets_amount
	elif difference < 0:
		raise ValueError('Difference below zero')
	elif difference > mass:
		raise ValueError('Difference is too hight')
	fake_busket = int(difference / coin_difference)
	return fake_busket

	
def main():
	answer = None
	while not answer:
		try:
			values = read_input()
			answer = calculate_answer(values)
			print(f'Basket full of fake coins is: №{answer}')
		except ValueError as e:
			logging.info(
				'Value error occured, is input values is valid? '
				f'Error body:\n{e.__str__()}'
			)
		except KeyboardInterrupt:
			print('\nbye')
			break


if __name__ == '__main__':
	main()