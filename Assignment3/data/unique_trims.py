

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1]
    trimmed_nucleotide=nucleotides[:len(nucleotides)-10]
    mr.emit_intermediate(trimmed_nucleotide,sequence_id)
	
def reducer(key, list_of_values):
	mr.emit(key)
			

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
