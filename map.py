# The map function recieve the row index as the key
# and the value as the value associated to the row
# We create a new key:value couple where the key
# is the column index and the value contains the rowIndex
# with the values associated to the columnindex and the
# rowindex

def map(rowIndex,values):
  columnIndex = 1
  for columnIndex in range(len(values)):
    key = columnIndex
    value = {rowIndex: values[columnIndex]}
  return {key:value}