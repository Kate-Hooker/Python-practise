value = True

while value ==True:
  print(value)
  value = False

nextvalue = "y"
count = 0

while nextvalue:
  count += 1
  print(count)
  if (count == 5):
    break
  else:
    value = 0
  continue
