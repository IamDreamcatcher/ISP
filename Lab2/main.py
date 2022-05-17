import argparse
import configparser
import sys

from lib.factory.create_serializer import create_serializer


def get_args():
    my_args_parser = argparse.ArgumentParser(description="Custom serializer")
    my_args_parser.add_argument("-config", dest="config_file", type=str, help="Your config")
    my_args_parser.add_argument("-in_file", dest="in_file", type=str, help="Input file")
    my_args_parser.add_argument("-out_file", dest="out_file", type=str, help="Output file")
    my_args_parser.add_argument("-in_type", dest="in_type", type=str, help="Input format type")
    my_args_parser.add_argument("-out_type", dest="out_type", type=str, help="Output format type")

    return my_args_parser.parse_args()


def convert(in_file, out_file, in_type, out_type):
    in_serializer = create_serializer(in_type)
    out_serializer = create_serializer(out_type)

    data = in_serializer.load(in_file)
    out_serializer.dump(data, out_file)


def main():
    args = get_args()
    in_file = ""
    out_file = ""
    in_type = ""
    out_type = ""

    if args.config_file is not None:
        config = configparser.ConfigParser()
        config.read(args.config_file)

        in_file = str(config["DEFAULT"]["in_file"])
        out_file = str(config["DEFAULT"]["out_file"])
        in_type = str(config["DEFAULT"]["in_type"])
        out_type = str(config["DEFAULT"]["out_type"])
    else:
        in_file = args.in_file
        out_file = args.out_file
        in_type = args.in_type
        out_type = args.out_type

    if in_file == "" or out_file == "" or in_type == "" or out_type == "" or in_type == out_type:
        print("Input format = output format or one of args is missing")
        sys.exit()
    else:
        convert(in_file, out_file, in_type, out_type)


if __name__ == '__main__':
    main()
