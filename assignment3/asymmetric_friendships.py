import MapReduce
import sys

"""
Social Network Asymmetric Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (person,friend)
    # value: 1 or -1
    key = (record[0],record[1])
    value = 1
    mr.emit_intermediate(key, value)
    key = (record[1],record[0])
    value = -1
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: friend
    for v in (key,list_of_values):
      if sum(list_of_values) != 0:
        if v != [1] and v != [-1]:
          mr.emit(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
