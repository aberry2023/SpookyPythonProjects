def odd_count(n):
    count_odd= [num for num in range(0,n) if num%2!=0]
    count_odd= len(count_odd)
    print(count_odd)
