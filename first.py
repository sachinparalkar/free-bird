text = ['Promising', 'Yves', 'that','home', 'on', 'Nobb']
[word[0] for word in text]

newlist = ['']*10

newlist = ['Odd' if i%2==1 else i for i in range(10) ]

start = -3
end = 3
steps = 11

x2 = [start + i*(end-start)/(steps-1) for i in range(steps)]
y2 = [i**2 for i in x2]

print(x2)
print(y2)
