# Enter your code here. Read input from STDIN. Print output to STDOUT

mydict = {}

n = raw_input()

for i in range(0, int(n)):
	inp = raw_input().split(" ")
	mydict[inp[0]] = inp[1]

query = raw_input()

while query != "":
	if query in mydict:
		print query + "=" + mydict[query]
	else:
		print "Not found"
	query = raw_input()