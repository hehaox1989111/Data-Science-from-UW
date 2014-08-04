import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

	person = record[0]
	friend=record[1]
	mr.emit_intermediate(person, [person,friend])
	mr.emit_intermediate(friend,[friend,person])
	
def reducer(key, list_of_values):
	pairs = [tuple(value) for value in list_of_values]
	all_set = set(pairs)

	dups_set = set([pair for pair in pairs if pairs.count(pair) > 1])

	asymmetric_friends = all_set ^ dups_set
	map(lambda pair: mr.emit(pair), asymmetric_friends)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
