import argparse
from fconvert.functions import convert_farenheit_to_cel

parser = argparse.ArgumentParser(description='Convert F to C')

parser.add_argument('farenheit', type=float, help='Value in Farenheit to convert')


args = parser.parse_args()

print(f"Farenheit: {args.farenheit}")
print(f"Celsius: {convert_farenheit_to_cel(args.farenheit)  }")