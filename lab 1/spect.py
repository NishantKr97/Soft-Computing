import csv
n=int(input("No. of rows(267): "))
m=int(input("No of columns(23): "))
iterations=100
l=0.61
bias=1/float(m)
w=[1/float(m) for i in range(m-1)]
data=[[]for i in range(n)]

with open('SPECT.csv', "r") as f_obj:
	reader=csv.reader(f_obj)
	i=-1
	for row in reader:
		if i!=-1:
			for col in row[1:]:
				data[i].append(float(col))
			data[i].append(row[0])
		i=i+1

def out(d):
	if d[m-1]=='No':
		return 0
	else:
		return 1

def test(d):
	z = 0
	for i in range(m-1):
		z = z + d[i]*w[i]
	z = z + bias
	if z>0:
		return 1
	else:
		return 0

def train(d):
	global bias
	global acc
	y=out(d)
	z=test(d)
	e=y-z
	if e:
		for i in range(len(w)):
			w[i]=w[i]+l*e*d[i]
		bias=bias+l*e*1
	else:
		acc=acc+1


for i in range(iterations):
	global acc
	acc=0
	for d in data:
		train(d)

print("Trained weights are:",w)
print("Bias: ",bias)

accuracy=acc/n *100
print("Accuracy: ",accuracy)