import csv
n=int(input("No. of rows(100): "))
m=int(input("No of columns(5): "))
l=1
E=1
bias=1/float(m)
w=[1/float(m) for i in range(m-1)]

data=[[]for i in range(n)]
with open('IRIS.csv', "r") as f_obj:
	reader=csv.reader(f_obj)
	i=-1
	for row in reader:
		if i!=-1:
			for col in row:
				if col==row[m-1]:
					data[i].append(col)
				else:
					data[i].append(float(col))
		i=i+1

def out(d):
	if d[m-1]=='Iris-setosa':
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
	y=out(d)
	z=test(d)
	e=y-z
	if e:
		for i in range(len(w)):
			w[i]=w[i]+l*e*d[i]
		bias=bias+l*e*1
	return e


while(E):
	E=0
	for d in data:
		E=E+abs(train(d))

print("Trained weights are:",w)
print("Bias: ",bias)

count=0
for d in data:
	if test(d)==out(d):
		count=count+1
accuracy=count/n *100
print("Accuracy: ",accuracy)
