import collections

thirdone = ''
with open("Lesson_6_task_3.txt") as inp_file:
    for line in inp_file:
        thirdone = thirdone + ' ' + line.rstrip()
print(thirdone)
thirdone_p = sorted(thirdone.split())
st = collections.Counter(thirdone_l for thirdone_l in thirdone_p)
for item in st:
    with open("Lesson_6_task_3.1.txt", 'a') as outFile:
        print(item+'     '+str(st[item]),file=outFile)
