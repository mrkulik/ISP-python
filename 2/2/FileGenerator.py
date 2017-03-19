import argparse
import string
import random


def field_generator(max_size=6, chars=string.ascii_lowercase, var=False):
    if var:
        return "".join(random.choice(chars) for _ in range(random.randint(1,max_size)))
    else:
        return "".join(random.choice(chars) for _ in range(max_size))


def string_generator(amount_of_strings, amount_of_fields, field_size, do=False, var=False):
    output_data = ""
    for line in range(0, amount_of_strings):
        for field in range(0, amount_of_fields):
            if do:
                output_data += field_generator(chars=string.digits, max_size=field_size, var=var)
            else:
                output_data += field_generator(max_size=field_size, var=var)
            if field != amount_of_fields-1:
                output_data += field_divider
        if line != amount_of_strings-1:
            output_data += string_divider
    return output_data

file_name = "file_input.txt"
amount_of_strings = 100
string_divider = "\n"
field_divider = "\t"
amount_of_fields = 5
field_size = 3


# argument parsing starts there
parser = argparse.ArgumentParser()
parser.add_argument("-f", help="output file name", type=str)
parser.add_argument("-sd", help="string divider", type=str)
parser.add_argument("-fd", help="field divider", type=str)
parser.add_argument("-sa", help="amount of strings to generate", type=int)
parser.add_argument("-fa", help="amount of fields in string", type=int)
parser.add_argument("-fs", help="field size in string", type=int)
parser.add_argument("-do", help="digits only generation", action="store_true")
parser.add_argument("-var", help="variable amount of fields in string (up to -fs parameter)", action="store_true")


args = parser.parse_args()
# argument parsing ends there

if args.f is not None:
    file_name = args.f

if args.sa is not None:
    amount_of_strings = args.sa

if args.sd is not None:
    string_divider = args.sd

if args.fd is not None:
    field_divider = args.fd

if args.fa is not None:
    amount_of_fields = args.fa

if args.fs is not None:
    field_size = args.fs


print("File generation parameters:")
print(" *Output file name: " + str(file_name))
print(" *Number of strings: " + str(amount_of_strings))
print(" *String size is " + str(amount_of_fields) + " fields")
print(" *Field size is " + str(field_size))
file = open(file_name, "w")
file.write(string_generator(amount_of_strings, amount_of_fields, field_size, args.do, args.var))
print("Generation completed, output file size is " + str(round(len(open(file_name).read())/1000000, 1)) + " MB")
