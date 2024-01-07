unsorted = input('List to be sorted: ')
unsorted = unsorted.split(",")
for times in range(len(unsorted)):
    for i in range(len(unsorted)-1):
        current = unsorted[i]
        next = unsorted[i+1]
        if current > next:
            unsorted[i+1] = current
            unsorted[i] = next
print(unsorted)
