#!/usr/bin/python

import argparse

import transposer


def parse_args():
    parser = argparse.ArgumentParser(
        description="command line args to assist with development")
    parser.add_argument('--in', dest='file_in', default=None, required=True,
                        help='file from which to read input data')
    parser.add_argument('--out', dest='file_out', default=None, required=True,
                        help='file to which results should be written')
    parser.add_argument('--delimiter', dest='delimiter', default=',',
                        help='the type of delmiter to read and write with' +
                               'defaults to \',\'')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.file_in and args.file_out:
        transposer.transpose(args.file_in, args.file_out, args.delimiter)
