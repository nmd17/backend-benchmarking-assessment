#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.
"""
__author__ = "nmd17"

import sys

def alphabetize(str):
    """ alphabetize Given a string, return a string that includes the same letters in
        alphabetical order """
        
    return "".join(sorted(str))

def find_anagrams(words):
    """ find_anagrams
        Return a dictionary with keys that are alphabetized words and values
        that are all words that, when alphabetized, match the key.
    """
    anagrams = {}
    for i in words:
        alpha = alphabetize(i)
        try:
            anagrams[alpha].append(i)
        except KeyError:
            anagrams[alpha] = [i]
            
    return anagrams

if __name__ == "__main__":
    # run find anagrams of first argument

    if len(sys.argv) < 2:
        print ("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print (find_anagrams(words))
