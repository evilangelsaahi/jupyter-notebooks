def day1(A, k):
    ac = it.combinations(A,2) # returns tuple of all possible combinations in given size 
    for i in ac:
        if sum(i) == k:
            return (True, i)
    else:
        return False

a = [10, 15, 3, 7]
day1(a, 17)
