def miniMaxSum(arr):
    arr.sort()
    total = sum(arr)
    minimum = total - arr[-1]
    maximum = total - arr[0]
    print(f'{str(minimum)} {str(maximum)}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
