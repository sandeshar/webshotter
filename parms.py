import argparse
import os

parse = argparse.ArgumentParser(
    "Take screenshot of mass domains/subdomains")
parse.add_argument('-f', '--filename', type=str, metavar='', required=True,
                   help="Name of file containing domains/subdomains")
parse.add_argument('-o', '--output', type=str, metavar='',
                   required=True, help="Name of folder to save the output")
parse.add_argument('-t', '--tabs', type=int, metavar='',
                   required=False, help="Number of tabs to open on browser(Currently in development)")
args = parse.parse_args()

if not os.path.exists(args.output):
    os.makedirs(args.output)