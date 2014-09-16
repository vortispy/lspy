#!/usr/bin/env python
# encoding: utf-8
import os

def ls():
    for file in os.listdir("."):
        if not file[0].startswith("."):
            print file,

if __name__ == '__main__':
    ls()
