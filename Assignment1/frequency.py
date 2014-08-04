import re
import sys
import json


def print_frequency(tweet_file):
    tweet=load_tweet(tweet_file)
    parse=parse_tweet(tweet)
    word_dict={}
    word_sum=0
    for word_list in parse:
        for word in word_list:
            word_sum+=1
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1
    for word in word_dict:
        print word, " ", float(word_dict[word]/word_sum)

def load_tweet(data):
    lst=[]
    line = data.readline()
    while len(line) is not 0:
	data1 = json.loads(line.strip())
	lst.append(data1)
	line = data.readline()
    return lst


def parse_tweet(tweet):
    pattern=re.compile(u'\w+')
    parse=[]
    for t in tweet:
        if 'text' in t.keys():
            words=pattern.findall(t['text'])
            parse.append(words)
    return parse


def main():
    tweet_file = open(sys.argv[1])
    
    print_frequency(tweet_file)


    tweet_file.close()

if __name__ == '__main__':
    main()
