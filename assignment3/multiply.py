import MapReduce
import sys

"""
Matrix multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: matrix_id
    # value: value
    matrix_id = record[0]
    value = record[3]
#    trimmed_nucleotides = nucleotides[0:len(nucleotides)-10]
    mr.emit_intermediate(matrix_id, value)

def reducer(key, list_of_values):
    # key: trimmed_nucleotides
    # value: sequence_id
      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
