def selectionSortDistance(array):
  vendor = len(array)
  for position in range(vendor-1):
    minRow = position
    for temp in range(position + 1 , vendor):
      if array[temp][0] < array[minRow][0]:
        minRow = temp
    array[position], array[minRow] = array[minRow], array[position]
  for i in range(len(array)):
    print(str(array[i][0]) + " Miles, £" + str(array[i][1]))
  return array


array = [[120, 150.12], [140, 180.1], [70, 250.02], [99, 398.72], [144, 205.42]] #index in position 0 is the number of miles a given distance is away fron start point, 1st index is cost
selectionSortDistance(array)
