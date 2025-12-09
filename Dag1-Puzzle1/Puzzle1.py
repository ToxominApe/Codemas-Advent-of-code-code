filename = "input.txt"

with open(filename) as input:
  n = 1
  

startWaarde = 50

testWaarde = "L32"

if "L" in testWaarde:
  startWaarde = startWaarde - 32
  print(startWaarde)
elif "R" in testWaarde:
  startWaarde = startWaarde + 32
