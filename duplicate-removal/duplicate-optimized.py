def remove_duplicates(arr):
  s = 0
  f = 1
  while f < len(arr):
    if arr[s] != arr[f]:
      s += 1
      arr[s] = arr[f]
    f += 1
  print(arr)
  return s + 1

print(remove_duplicates([1, 2, 2, 3, 3, 3, 5]))