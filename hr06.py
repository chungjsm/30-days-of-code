# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
words = []

for i in range(0, n):
    words.append(raw_input().strip())

for word in words:
    output1 = ""
    output2 = ""
    for j in range(0,len(word)):
        if j % 2 == 0:
            output1 += word[j]
        else:
            output2 += word[j]
    print output1 + " " + output2