#!/usr/bin/env python
# encoding: utf-8
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", default=".", nargs="?")
args = parser.parse_args()

def ls():
    path = args.path
    for file in os.listdir(path):
        if not file[0].startswith("."):
            print file,

if __name__ == '__main__':
    ls()
