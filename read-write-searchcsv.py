import csv
with open('student.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)
file.close()

f=open("student.csv",'a',newline="")
csv_writer=csv.writer(f,delimiter=',')
while True:
    a=input("enter rno")
    b=input("enter class")
    c=input("enter %")
    l=[a,b,c]
    csv_writer.writerow(l)
    ask=input("do u want to enter more values")
    if ask=='no':
        break
f.close()


searchfile = open('student.csv', 'r')
reader = csv.reader(searchfile, delimiter = ',')
ab = input("eneter")
for row in reader:
    if a in row[0] or a in row[1]:
        print(row)
