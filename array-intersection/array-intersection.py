def intersection(arr1, arr2):
  fp = sp = 0
  new_arr = []
  while fp < len(arr1) and sp < len(arr2):
    if arr1[fp] == arr2[sp]:
      new_arr.append(arr1[fp])
      sp += 1
      fp += 1
    elif arr1[fp] > arr2[sp]:
      sp += 1
    else:
      fp += 1
  return new_arr 

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(intersection(arr1, arr2))