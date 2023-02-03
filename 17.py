fileName = 'marks.txt'
keyFileName = 'key.txt'

with open(keyFileName, 'r') as f:
    answerKey = f.readline().strip().split(' ')[1:]

students = {}
with open(fileName, 'r') as f:
    for line in f:
        x = line.strip().split(' ')
        students[x[0]] = x[1:]

studentMarks = {}
for name in students.keys():
    marks = sum(answerKey[i] == students[name][i]
                for i in range(len(answerKey)))
    studentMarks[name] = marks
    print(name, ":", marks)

topScore = max(studentMarks.values())
topScorer = [name for name in studentMarks if studentMarks[name] == topScore]

print("Top Score =", topScore)
for student in topScorer:
    print("Top Scorer :", student)
