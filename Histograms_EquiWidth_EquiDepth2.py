import csv

incomeArray = []
equiWidthBinRanges = []
equiWidthBinNumtuples = []
equiDepthBinRanges = []
equiDepthBinNumtuples = []


def equiwidth():
    distance = max(incomeArray) - min(incomeArray)
    bins = 100
    equiWidthBorders = distance / bins
    equiWidthMin = min(incomeArray)

    incomeArray.sort()
    index = 0

    for y in range(0, bins):
        numtuplesCounter = 0
        equiWidthMax = equiWidthMin + equiWidthBorders
        equiWidthMax = round(equiWidthMax, 2)

        while equiWidthMin <= incomeArray[index] < equiWidthMax:
            if index < len(incomeArray) - 1:
                index += 1
            numtuplesCounter += 1

        equiWidthBinRanges.append([equiWidthMin, equiWidthMax])
        equiWidthMin = equiWidthMax
        equiWidthBinNumtuples.append(numtuplesCounter)


def equidepth():

    bins = 100
    numtuplesForEachBin = int(len(incomeArray) / bins)
    equiDepthMin = min(incomeArray)
    index = 0
    for x in range(0, bins):
        numtuplesCounter = 0

        while numtuplesCounter < numtuplesForEachBin:
            index += 1
            numtuplesCounter += 1

        equiDepthMax = incomeArray[index]

        equiDepthBinRanges.append([equiDepthMin, equiDepthMax])
        equiDepthMin = equiDepthMax
        equiDepthBinNumtuples.append(numtuplesCounter)


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

a = float(input('Please give the number of a: '))
b = float(input('Please give the number of b: '))

incomeArray.sort()
actualResults = 0

for i in incomeArray:
    if a <= i < b:
        actualResults += 1

equiwidth()
equidepth()
equiWidthEstimated = 0
equiDepthEstimated = 0

# EQUI-WIDTH

for i in range(len(equiWidthBinRanges)):
    if not (a > equiWidthBinRanges[i][1] or b < equiWidthBinRanges[i][0]):
        if a <= equiWidthBinRanges[i][0] and b >= equiWidthBinRanges[i][1]:
            equiWidthEstimated += equiWidthBinNumtuples[i]
        else:
            if a >= equiWidthBinRanges[i][0]:
                leftEdge = a
            else:
                leftEdge = equiWidthBinRanges[i][0]
            if b <= equiWidthBinRanges[i][1]:
                rightEdge = b
            else:
                rightEdge = equiWidthBinRanges[i][1]
            commonAreaPercent = (rightEdge - leftEdge) / (equiWidthBinRanges[i][1] - equiWidthBinRanges[i][0])
            equiWidthEstimated += commonAreaPercent * equiWidthBinNumtuples[i]

# EQUI-DEPTH

for i in range(len(equiDepthBinRanges)):
    if not (a > equiDepthBinRanges[i][1] or b < equiDepthBinRanges[i][0]):
        if a <= equiDepthBinRanges[i][0] and b >= equiDepthBinRanges[i][1]:
            equiDepthEstimated += equiDepthBinNumtuples[i]
        else:
            if a >= equiDepthBinRanges[i][0]:
                leftEdge = a
            else:
                leftEdge = equiDepthBinRanges[i][0]
            if b <= equiDepthBinRanges[i][1]:
                rightEdge = b
            else:
                rightEdge = equiDepthBinRanges[i][1]
            commonAreaPercent = (rightEdge - leftEdge) / (equiDepthBinRanges[i][1] - equiDepthBinRanges[i][0])
            equiDepthEstimated += commonAreaPercent * equiDepthBinNumtuples[i]

print()
print('Equiwidth estimated results: ' + str(equiWidthEstimated))
print('Equidepth estimated results: ' + str(equiDepthEstimated))
print('Actual results: ' + str(actualResults))
