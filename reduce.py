# The reduce function recieve the new rowIndex (previously columnIndex)
# as the key and an array containing the new columnIndex and the
# value of the corresponding element in the matrix
# It then create a key: value couple where the key is the new rowindex
# and the values are elements from the matrix
# All together the output form the transposed version of the input of
# the map function

def reduce(key,values):
  valuesT = []
  for x in values:
    valuesT[x.key] = x.value
  rowIndexT = key
  return {rowIndexT: valuesT}