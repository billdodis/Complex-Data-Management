import csv

incomeArray = []

with open("./acs2015_census_tract_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    counter = 0

    for row in csvreader:
        if counter == 0:
            incomeIndex = row.index('Income')
        else:
            if row[incomeIndex] != '':
                incomeArray.append((float(row[incomeIndex])))
        counter = counter + 1

print('Valid income values: ' + str(len(incomeArray)))
print('Minimum Income: ' + str(min(incomeArray)))
print('Maximum Income: ' + str(max(incomeArray)))

distance = max(incomeArray) - min(incomeArray)
bins = 100
equiWidthBorders = distance/bins
equiWidthMin = min(incomeArray)

print('equi-width:')
incomeArray.sort()
index = 0
finalTuples = 0

for i in range(0, bins):
    numtuplesCounter = 0
    equiWidthMax = equiWidthMin + equiWidthBorders
    equiWidthMax = round(equiWidthMax, 2)

    while equiWidthMin <= incomeArray[index] < equiWidthMax:
        if index < len(incomeArray) - 1:
            index += 1
        numtuplesCounter += 1

    finalTuples += numtuplesCounter
    print('bin : ' + str(i))
    print('range:  [' + str(equiWidthMin) + ', ' + str(equiWidthMax) + '), ' + 'numtuples: ' + str(numtuplesCounter))
    equiWidthMin = equiWidthMax

print("Numtuples used in equi-width: " + str(finalTuples))

print('equi-depth:')

bins = 100
numtuplesForEachBin = int(len(incomeArray)/bins)
equiDepthMin = min(incomeArray)
index = 0
finalTuples = 0

for i in range(0, bins):
    numtuplesCounter = 0
    while numtuplesCounter < numtuplesForEachBin:
        index += 1
        numtuplesCounter += 1
    equiDepthMax = incomeArray[index]
    print('bin : ' + str(i))
    print('range:  [' + str(equiDepthMin) + ', ' + str(equiDepthMax) + '), ' + 'numtuples: ' + str(numtuplesCounter))
    equiDepthMin = equiDepthMax
    finalTuples += numtuplesCounter

print("Numtuples used in equi-depth: " + str(finalTuples))
