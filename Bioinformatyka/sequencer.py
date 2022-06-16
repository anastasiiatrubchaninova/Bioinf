import sys


nextIndex = 0
prevIndex = 0


# leci po tablicy odległości i szuka następnego słowa, po czym dopisuje ostatnią literę
def checkNext(index):
    used[index] = 1
    possibleNext = []
    global result
    if len(result) >= N:
        return
    for j in range(len(dist[index])):
        if dist[index][j] == maxCovers[index] and used[j] == 0:
            possibleNext.append(j)
    if len(possibleNext) == 0:
        maxCovers[index] -= 1
        global nextIndex
        nextIndex = index
    else:
        if len(possibleNext) > 1:
            nextChoice = checkAhead(possibleNext)
        else:
            nextChoice = possibleNext[0]
        result += dna[nextChoice][maxCovers[index]:]
        checkNext(nextChoice)
    return


def checkPrev(index):
    used[index] = 1
    possibleNext = []
    global result
    if len(result) >= N:
        return
    for j in range(len(dist[index])):
        if distPrev[index][j] == maxCovers[index] and used[j] == 0:
            possibleNext.append(j)
    if len(possibleNext) == 0:
        maxCovers[index] -= 1
        global prevIndex
        prevIndex = index
    else:
        if len(possibleNext) > 1:
            nextChoice = checkAhead(possibleNext)
        else:
            nextChoice = possibleNext[0]
        result = dna[nextChoice][0:len(dna[nextChoice]) - maxCovers[index]] + result
        checkPrev(nextChoice)
    return


def checkAhead(indexList):
    nextMax = 0
    for index in indexList:
        for j in range(len(dist[index])):
            if nextMax < dist[index][j] < 10 and used[j] == 0:
                nextMax = dist[index][j]
                nextIx = index
                if nextMax == 9:
                    return nextIx
    return nextIx


file = open(sys.argv[1], "r")
N = int(sys.argv[2])
L = 10
dna = file.readlines()

print(dna)
# Usunięcie \n z końca każdego słowa
for i in range(len(dna) - 1):
    dna[i] = dna[i][:-1]
print(dna)
dist = [[0 for i in range(len(dna))] for j in range(len(dna))]
distPrev = [[0 for i in range(len(dna))] for j in range(len(dna))]


index = 0
#porównuje każde słowo z każdym, wyliczając maksymalne pokrycie
for d1 in dna:
    count = 0
    for d2 in dna:
        for i in range(len(d1)):
            # jeśli litera pokrywa się z pierwszą literą drugiego słowa, zaczyna sprawdzać ile kolejnych też się pokrywa
            if d1[i] == d2[0]:
                current = 1
                for j in range(i+1, len(d1)):
                    if d1[j] == d2[current]:
                        current += 1
                    else:
                        if dist[index][count] < current:
                            dist[index][count] = current
                        break
                if dist[index][count] < current:
                    dist[index][count] = current
        for i in range(len(d1) - 1, -1, -1):
            # jeśli litera pokrywa się z pierwszą literą drugiego słowa, zaczyna sprawdzać ile kolejnych też się pokrywa
            if d1[i] == d2[len(d2) - 1]:
                current = 1
                for j in range(i-1, -1, -1):
                    if d1[j] == d2[len(d2) - 1 - current]:
                        current += 1
                    else:
                        if distPrev[index][count] < current:
                            distPrev[index][count] = current
                        break
                if distPrev[index][count] < current:
                    distPrev[index][count] = current

        count += 1
    index += 1


used = [0 for i in range(len(dna))]
maxCovers = [9 for i in range(len(dna))]
result = dna[0]


while len(result) < N and 0 in used:
    checkNext(nextIndex)
    checkPrev(prevIndex)

print("Rozwiązanie: " + result)
counter = 0
for i in used:
    if i == 1:
        counter += 1
print("Różne słowa użyte w rozwiązaniu: " + str(counter))
print("Długość rozwiązania: " + str(len(result)))
