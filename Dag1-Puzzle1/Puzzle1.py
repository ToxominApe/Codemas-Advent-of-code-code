startWaarde = 50

testWaarde = "L32"

if testWaarde.find("L") != -1:
  startWaarde = startWaarde + 32
  print(startWaarde)
elif testWaarde.find("R") != -1:
  startWaarde = startWaarde - 32