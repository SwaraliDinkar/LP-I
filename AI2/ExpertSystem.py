import sys

fileName = sys.argv[1]
symptomDictionary = {}
diseaseMatch = {}

def read(dataFileName=fileName):
    dataFile = open(dataFileName, 'r')
    symptomsList = []

    for line in dataFile:
        tokens = line.split(',')
        diseaseName = tokens[0][1:-1]

        for i in range(1, len(tokens)):
            symptomsList.append(tokens[i].strip())
        symptomDictionary[diseaseName] = symptomsList
 

def detectDisease():
    symptoms = input('Enter the symptoms(comma seperated): : ')
    s = symptoms.split(',')


    for index in range(0, len(s)):
        s[index] = s[index].strip().lower()

    print('The given symptoms are: : ', s)

    totalCount = 0.0

    for i in symptomDictionary.keys():
        count = 0.0
        k = symptomDictionary[i]
        for j in s:
            if j in k:
                count += 1

        if count > 0:
            totalCount += count
            diseaseMatch[i] = count

    for key, value in (diseaseMatch.items()):
        print('The possibility of having %s is %.2f %%' % (key, (value * 100)/totalCount))



read(fileName)
detectDisease()
