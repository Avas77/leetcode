def remove_duplicates(arr):
  f = s = 0
  unique = set()
  while f < len(arr):
    if arr[f] not in unique:
      unique.add(arr[f])
      arr[s] = arr[f]
      f += 1
      s += 1
    else:
      f += 1
  return len(unique)

print(remove_duplicates([1, 1, 1]))