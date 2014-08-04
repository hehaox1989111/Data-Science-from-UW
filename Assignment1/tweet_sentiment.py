import sys
import re
import json


def print_senitments(sent_file, tweet_file):
    tweet=load_tweet(tweet_file)
    parse=parse_tweet(tweet)
    sent_scores=SentimentScore(sent_file)
    for word_list in parse:
        summed=[]
        for t in word_list:
            if t in sent_scores:
                summed.append(sent_scores[t])
            else:
                summed.append(0)
        print sum(summed)   
    

def SentimentScore(sent_s):
    scores = {} # initialize an empty dictionary
    for line in sent_s:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores;

   
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
    


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    print_senitments(sent_file,tweet_file)
    

    
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()
