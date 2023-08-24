def fibonacci_sequence(n):
    arr = [0,1]
        
    while len(arr) < n:
        arr.append(arr[-2] + arr[-1])
    return arr

print(fibonacci_sequence(10))