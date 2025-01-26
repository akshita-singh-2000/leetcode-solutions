
def minimumLength(self, s: str) -> int:
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    sum= 0           
    for val in dict1.values():
        if val % 2 == 0:
            sum+= 2
        else:
            sum+=1
    return sum