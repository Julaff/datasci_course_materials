import MapReduce
import sys

"""
DNA sequences trimming and removing duplicates in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: nucleotides
    # value: sequence_id
    nucleotides = record[1]
    sequence_id = record[0]
    trimmed_nucleotides = nucleotides[0:len(nucleotides)-10]
    mr.emit_intermediate(trimmed_nucleotides, sequence_id)

def reducer(key, list_of_values):
    # key: trimmed_nucleotides
    # value: sequence_id
      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
