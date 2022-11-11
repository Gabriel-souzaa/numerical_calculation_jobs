#Nome : Gabriel Freitas de souza
#RA   : N663HJ1
#Turma: CC2P12

## Trabalho 01 de CN: Resolução de Sistemas Lineares ##

import csv;
import numpy;

fileName = 'equations.csv'

def main():
  readFileCsV()

def readFileCsV():
  with open(fileName, "r") as file:
    file_csv = csv.reader(file, delimiter = ",")
    calculateLinearSystem(file_csv)

def calculateLinearSystem(file):
  system = []
  resultSystem = []

  for i,line in enumerate(file):
    lineSystem = []
    resultSystem.append(float(line[-1]))
    for itemLine in list(line):
      if line[-1] != itemLine:
        lineSystem.append(float(itemLine))
    system.append(lineSystem)
      
  result = numpy.linalg.solve(numpy.array(system), numpy.array(resultSystem))
  print(result)

main()

