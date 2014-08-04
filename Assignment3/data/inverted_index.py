import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    key = record[0]
    value = record[1]
    terms = value.split()
    map(lambda term: mr.emit_intermediate(term, key), terms)

def reducer(key, list_of_values):

    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
