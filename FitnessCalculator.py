#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as mplot

# open both an appending and a reading version of the tss data
data = open("data.txt", "a+")
dataRead = open("data.txt", "r")
dataRead = dataRead.read()
dataRead = dataRead.split("\n")

# open both a writing and a reading version of the tss data
fitNums = open("fitNums.txt", "w+")
fitNumsRead = open("fitNums.txt", "r")
fitNumsRead = fitNumsRead.read()
fitNumsRead = fitNumsRead.split("\n")

# separate fitness numbers values
for index in range(0, len(fitNumsRead)):
    if len(fitNumsRead[index]) == 0:
        del(fitNumsRead[index])
        continue
    fitNumsRead[index] = fitNumsRead[index].split(",")
    # convert the data into numbers
    fitNumsRead[index][0] = float(fitNumsRead[index][0])
    fitNumsRead[index][1] = float(fitNumsRead[index][1])
    fitNumsRead[index][2] = float(fitNumsRead[index][2])
    fitNumsRead[index][4] = float(fitNumsRead[index][4])
    fitNumsRead[index][6] = float(fitNumsRead[index][6])
    fitNumsRead[index][8] = float(fitNumsRead[index][8])

# separate tss data values
for index in range(0, len(dataRead)):
    if len(dataRead[index]) == 0:
        del(dataRead[index])
        continue
    dataRead[index] = dataRead[index].split(",")
    # convert the data into numbers
    dataRead[index][0] = float(dataRead[index][0])
    dataRead[index][1] = float(dataRead[index][1])
    dataRead[index][2] = float(dataRead[index][2])
    dataRead[index][3] = float(dataRead[index][3])

# initialize tss for looping purposes
tss = 0

# define the functions to make this easy
def calCTL(tss, ctly=0, TCc=42):
    ctl = ctly + ((tss - ctly) / TCc)
    return ctl
def calATL(tss, atly=0, TCa=10):
    atl = atly + ((tss - atly) / TCa)
    return atl
def calTSB(ctl, atl):
    tsb = ctl - atl
    return tsb

# see if you need to input data or not
startingPoint = input("Do you need to input data? (y = yes; n = no)  ")
startingPoint = startingPoint.lower()

if startingPoint == "y":
    while float(tss) != -1:
        date = input("Workout Date (MM/DD/YY):\t")
        # separate the date
        month = ''.join(date[0]+date[1])
        day = ''.join(date[3]+date[4])
        year = ''.join(date[6]+date[7])

        tss = input("Workout TSS (Enter -1 to finish entry):\t")
        print ("\n")

        # add that new data to the data file
        if float(tss) != -1:
            data.write(month + ", " + day + ", " + year + ", " + tss + "\n")
            dataRead.append([float(month), float(day), float(year), float(tss)])

# initialize ctl, atl, and tsb
ctl = 0
atl = 0
tsb = 0
# save a copy of them as strings
ctlString = str(ctl)
atlString = str(atl)
tsbString = str(tsb)
# add the new numbers to both the text file and the already-opened list
fitNums.write(str(dataRead[0][0]) + ", " + str(dataRead[0][1]) + ", " + str(dataRead[0][2]) + ", Fitness, " + ctlString + ", Fatigue, " + atlString + ", Form, " + tsbString + "\n")
fitNumsRead.append([dataRead[0][0], dataRead[0][1], dataRead[0][2], "Fitness", ctl, "Fatigue", atl, "Form", tsb])


# iterate through the data to calculate all training values
for index in range(1, 10):
    # calculate the next day's numbers
    ctl = calCTL(dataRead[index][3], fitNumsRead[index-1][4], index)
    atl = calATL(dataRead[index][3], fitNumsRead[index-1][6], index)
    tsb = calTSB(ctl, atl)
    # save a copy of them as strings
    ctlString = str(ctl)
    atlString = str(atl)
    tsbString = str(tsb)
    # add the new numbers to both the text file and the already-opened list
    fitNums.write(str(dataRead[index][0]) + ", " + str(dataRead[index][1]) + ", " + str(dataRead[index][2]) + ", Fitness, " + ctlString + ", Fatigue, " + atlString + ", Form, " + tsbString + "\n")
    fitNumsRead.append([dataRead[index][0], dataRead[index][1], dataRead[index][2], "Fitness", ctl, "Fatigue", atl, "Form", tsb])
for index in range(10, 42):
    # calculate the next day's numbers
    ctl = calCTL(dataRead[index][3], fitNumsRead[index-1][4], index)
    atl = calATL(dataRead[index][3], fitNumsRead[index-1][6])
    tsb = calTSB(ctl, atl)
    # save a copy of them as strings
    ctlString = str(ctl)
    atlString = str(atl)
    tsbString = str(tsb)
    # add the new numbers to both the text file and the already-opened list
    fitNums.write(str(dataRead[index][0]) + ", " + str(dataRead[index][1]) + ", " + str(dataRead[index][2]) + ", Fitness, " + ctlString + ", Fatigue, " + atlString + ", Form, " + tsbString + "\n")
    fitNumsRead.append([dataRead[index][0], dataRead[index][1], dataRead[index][2], "Fitness", ctl, "Fatigue", atl, "Form", tsb])
for index in range(42, len(dataRead)):
    # calculate the next day's numbers
    ctl = calCTL(dataRead[index][3], fitNumsRead[index-1][4])
    atl = calATL(dataRead[index][3], fitNumsRead[index-1][6])
    tsb = calTSB(ctl, atl)
    # save a copy of them as strings
    ctlString = str(ctl)
    atlString = str(atl)
    tsbString = str(tsb)
    # add the new numbers to both the text file and the already-opened list
    fitNums.write(str(dataRead[index][0]) + ", " + str(dataRead[index][1]) + ", " + str(dataRead[index][2]) + ", Fitness, " + ctlString + ", Fatigue, " + atlString + ", Form, " + tsbString + "\n")
    fitNumsRead.append([dataRead[index][0], dataRead[index][1], dataRead[index][2], "Fitness", ctl, "Fatigue", atl, "Form", tsb])

# print the current numbers
print("Fitness: " + ctlString + "\tFatigue: " + atlString + "\tForm: " + tsbString)

# initialize empty axis sets for each data type
xaxis = []
yaxisfit = []
yaxisfat = []
yaxisform = []
yaxiszero = []

for index in range(0,len(fitNumsRead)):
    # create x-axis lists for each data type
    xaxis.append(index)
    # create y-axis lists for each data type
    yaxisfit.append(fitNumsRead[index][4])
    yaxisfat.append(fitNumsRead[index][6])
    yaxisform.append(fitNumsRead[index][8])
    yaxiszero.append(0)

mplot.plot(xaxis, yaxisfit, color="blue")
mplot.plot(xaxis, yaxisfat, color="red")
mplot.plot(xaxis, yaxisform, color="green")
mplot.plot(xaxis, yaxiszero, color="black")
mplot.show()
