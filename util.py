#import urllib2
import sys
from bs4 import BeautifulSoup
import os
import re
import pickle
import httpx

async def get_content(link):
    # webUrl = urllib2.urlopen(link)
    # result = webUrl.read()
    # asyncio will not really work if you are not using library which supports async
    async with httpx.AsyncClient() as client:
        result = await client.get(link)
    return result.text

def write_content(*args):
    # TODO:
    COUNT = args[4]
    COUNT = COUNT + 1
    file = open(args[-2] + "/" + str(COUNT) + ".html","w")
    data = args[0] + "\n" + args[1] + "\n" + args[2]
    file.write(data)
    file.close()
    return COUNT

def find_links(content, URLList):
    soup = BeautifulSoup(content, 'html.parser')
    for link in soup.find_all('a'):
        if link not in URLList:
            URLList.append(link.get('href'))

def store_to_file(file, map):
    with open(file,'w') as f:
        f.write(pickle.dumps(map))

def read_from_file(file):
    f = open(file,'r')
    map = pickle.load(f)
    return map

def find_occurance(word, words):
    return words.count(word)

# Creating a datastructure to store the data from different files
def store_to_ds(words, file, map):
    for word in set(words):
        ### calculate the frequency of the current word
        occurance = find_occurance(word, words)
        #for each file the dict should get appended with filename and occurance
        if word in map:
            map[word]['tot_occur'] = map[word]['tot_occur'] + occurance
            map[word][file] = occurance
        else:
            map[word] = {}
            map[word]['tot_occur'] = occurance
            map[word][file] = occurance

# parsing data into list of words
def parse_data_into_words(data):
    result = []
    lines = data.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line:
            words = line.split()
            [result.append(word.strip()) for word in words]
    return result

#Remove html tags from a string
def get_data_without_tags(file):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', file)


