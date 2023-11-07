print("\nWelcome to ABS 1!")
print("Hello " * 5)
nameFilename = ".experimentalOutputs/nameFile"
def userQueryYesNo(queryString):
  print(queryString + " (Y/n)")
  response = input()
  if response == "Y":
    return True
  else:
    return 0
def userQueryForString(queryString):
  print(queryString)
  queryResponse = input()
  return queryResponse
def getName(): 
  if userQueryYesNo("Would you like to enter your name?"):
    yourName = userQueryForString("What's your name?")
    nameFile = open(nameFilename, "a")
    nameFile.write("\n"+yourName)
    print("Your name has been recorded")
    nameFile.close()
def printNames():
  nameFile = open(nameFilename)
  print("\nThe names that have been recorded are:")
  print()
  allNames = nameFile.readlines()
  for x in allNames:
    #print(x)
    print(x.removesuffix("\n"))
while 1 == 1:
  print()
  getName()
  printNames()