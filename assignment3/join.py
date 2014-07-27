import MapReduce
import sys

"""
Relational Join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_list
    # value: line_list
    order_list = list_of_values[0]
    line_list = list_of_values[1:]
    for i in range(len(line_list)):
      mr.emit(list(order_list + line_list[i-1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
