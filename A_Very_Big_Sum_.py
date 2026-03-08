def aVeryBigSum(arr):
    total = 0
    for n in arr:
        total += n
    return total

print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))
