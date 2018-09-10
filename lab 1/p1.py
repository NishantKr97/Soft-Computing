import csv
n=int(input("No. of rows: "))
m=int(input("No of columns: "))
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

def test(d):
	z = 0
	for i in range(m-1):
		z = z + d[i]*w[i]
		print(z)
	z = z + bias
	if z>0:
		return 1
	else:
		return 0


bias=1
w=[1/(n+1) for i in range(m-1)]
print(data[0])
print(test(data[0]))



