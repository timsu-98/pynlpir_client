#!/usr/bin/python3
import os
import sys
from logging import getLogger

from pynlpir_client import PyNLPIRClient

def main():
    argv = sys.argv[1:]

    logger = getLogger('pynlpir_client')

    print('\033[1;33mRunning...\033[0m')

    read_dirs = ['text']
    output_dir = 'output'

    client = PyNLPIRClient(read_dirs, output_dir)

    client.analyse_files(segment=True, get_key_words=True, weighted=True)

    client.close_client()

    print('\033[1;32mFinished.\033[0m')

if __name__=="__main__":
    main()