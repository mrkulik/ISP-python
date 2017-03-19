import argparse
import Task_1_sort as T1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input', type=str)
    parser.add_argument('-out', '--output', type=str)
    parser.add_argument('-k', '--key', type=int)
    parser.add_argument('-ls', '--line_separator', type=str)
    parser.add_argument('-fs', '--field_separator', type=str)
    parser.add_argument('-n', '--numeric', action="store_true")
    parser.add_argument('-ch', '--check', action='store_true')
    parser.add_argument('-bs', '--buffer_size', type=int)
    parser.add_argument('-rev', '--reverse', action='store_true')
    args = parser.parse_args()

    arg_reverse = True if args.reverse else False

    file_output = args.input if args.output is None else args.output

    buffer_size = 45 if args.buffer_size is None else args.buffer_size

    field_separator = '\t' if args.field_separator is None else args.field_separator

    line_separator = '\n' if args.line_separator is None else args.line_separator

    key = 1 if args.key is None else args.key

    if args.check:
        T1.check(args.input)
    else:
        T1.sort(args.input, file_output, buffer_size, arg_reverse, line_separator, field_separator, key)


if __name__ == "__main__":
    main()
