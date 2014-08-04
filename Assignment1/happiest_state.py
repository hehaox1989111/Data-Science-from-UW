import sys
import re
import json

state_mapping = { 
	"alabama": "al",
	"alaska": "ak",
	"arizona": "az",
	"arkansas": "ar",
	"california": "ca",
	"colorado": "co",
	"connecticut": "ct",
	"delaware": "de",
	"florida": "fl",
	"georgia": "ga",
	"hawaii": "hi",
	"idaho": "id",
	"illinois": "il",
	"indiana": "in",
	"iowa": "ia",
	"kansas": "ks",
	"kentucky": "ky",
	"louisiana": "la",
	"maine": "me",
	"maryland": "md",
	"massachusetts": "ma",
	"michigan": "mi",
	"minnesota": "mn",
	"mississippi": "ms",
	"missouri": "mo",
	"montana": "mt",
	"nebraska": "ne",
	"nevada": "nv",
	"new hampshire": "nh",
	"new jersey": "nj",
	"new mexico": "nm",
	"new york": "ny",
	"north carolina": "nc",
	"north dakota": "nd",
	"ohio": "oh",
	"oklahoma": "ok",
	"oregon": "or",
	"pennsylvania": "pa",
	"rhode island": "ri",
	"south carolina": "sc",
	"south dakota": "sd",
	"tennessee": "tn",
	"texas": "tx",
	"utah": "ut",
	"vermont": "vt",
	"virginia": "va",
	"washington": "wa",
	"west virginia": "wv",
	"wisconsin": "wi",
	"wyoming": "wy" }

token_regex = re.compile(r'\w+')
abbr_state_regex = re.compile(r'\w{2}')







def parse_tweet(tweet):
    pattern=re.compile(u'\w+')
    parse=[]
    for t in tweet:
        if 'text' in t.keys():
            words=pattern.findall(t['text'])
            parse.append(words)
    return parse




def load_tweet(data):
    lst=[]
    line = data.readline()
    while len(line) is not 0:
	data1 = json.loads(line.strip())
	lst.append(data1)
	line = data.readline()
    return lst


def SentimentScore(sent_s):
    scores = {} # initialize an empty dictionary
    for line in sent_s:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores;



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    print_senitments(sent_file,tweet_file)


    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()
