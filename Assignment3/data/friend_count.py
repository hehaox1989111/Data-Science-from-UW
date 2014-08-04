import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

	key = record[0]
	mr.emit_intermediate(key, 1)
	
	
def reducer(key, list_of_values):
	total=0
	for l in list_of_values:
		total+=1
	mr.emit((key,total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
