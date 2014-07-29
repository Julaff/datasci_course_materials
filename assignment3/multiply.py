import MapReduce
import sys

"""
Matrix multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i,j) then (j,k)
    # value: A[i,j] then B[j,k]
#    print record[3]
    tablename = record[0]
    if tablename == 'a':
      for k in range(5):
        key = (record[1],k)
        value = (record[2],record[3])
        mr.emit_intermediate(key, value)

    elif tablename == 'b':
      for i in range(5):
        key = (i,record[2])
        value = (record[1],record[3])
        mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
#    print 0
    # key: (i,k)
    # value: Sum_j(A[i,j]*B[j,k])
    l = []
    for c in range(len(list_of_values)):
      l.append(list_of_values[c][0])
    print l
#      mr.emit((key,list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
