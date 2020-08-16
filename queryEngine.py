"""
Use index.dat and finds the occurance of the given word from top 10 docs
"""
import sys
import math
from util import read_index_from_file
from collections import defaultdict


def get_info(index,*args):
    for word in args:
        return index[word].items()
        
def display(data):
    for d in data:
        with open("/home/ankit/Desktop/ayushi/tiny-search-engine/files/" + d[0], 'r') as f:
            url = f.readline()
            print "Document ID:" + d[0] + " URL:" + url.strip()
        
def foo(arg):
    return arg[1]

def rank(args):
    final_data = []
    result = {}
    for arg in args:
        result.update(dict(arg))
    return sorted(result.items(), key=foo, reverse=True)

def get_details(index, word):
    # find the file and occurance of all files from index for a word
    if word in index:
        del index[word]["tot_occur"]
    return index.get(word,{}).items()

def main():
    if len(sys.argv) != 2:
        print("Wrong Info passed")
        sys.exit(1)

    output = []
    words = sys.argv[1]
    index = read_from_file("index.dat")

    # find the file and occurance of all files from index for a word
    for word in words.split(' '):
    	output.append(get_details(index, word))
    # ranking = sum the frequency and sort
    result = rank(output)
    display(result)
    
if __name__ == '__main__':
    main()

