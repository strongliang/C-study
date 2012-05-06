f = open('/Users/Z/Documents/dev/python/algo/IntegerArray.txt', 'r')

numbers = []
for line in f:
    numbers.append(int(line))
    
count = 0

def msort(list, start, end):
    global count
    if start == end:
        return
    elif start == end - 1:
        if list[start] > list[end]:
            list[start], list[end] = list[end], list[start]
            count += 1
        return
    else:        
        mid = (end + start) / 2
#        print start, mid, end
        msort(list, start, mid)
        msort(list, mid+1, end)
#        print list[start:mid+1], list[mid+1:end+1]
        
        la = list[start:mid+1]
        lb = list[mid+1:end+1]
        lm = []
        i, j = 0, 0
        while i<len(la) and j<len(lb):
            if la[i] <= lb[j]:
                lm.append(la[i])
                i += 1
            else:
                # this is the tricky part, it's not len(la) - 1 -i
                # because this la[i] is also an inversion
                count += len(la) - i 
                lm.append(lb[j])
                j += 1
        while i < len(la):
            lm.append(la[i])
            i += 1
        while j < len(lb):
            lm.append(lb[j])
            j += 1
        
        i = 0
        j = start            
        while i < len(lm):
            list[j] = lm[i]
            i += 1
            j += 1            

        
#test = [10, 2, 4, 3, 5, 6, 4]

test = [3, 2, 1, 6, 5, 4]
#msort(numbers, 0, len(numbers)-1)
#print 'final = ', numbers        

msort(test, 0, len(test)-1)
print test
print 'inversion count =', count

