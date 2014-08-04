import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

	key = record[1]
	mr.emit_intermediate(key, record)
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
	order=list_of_values[0]
	line_of_item=list_of_values[1:]
	for l in line_of_item:
		mr.emit(order+l)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
