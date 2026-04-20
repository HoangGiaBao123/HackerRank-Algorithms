def plusMinus(arr):
    positive = [p for p in arr if p > 0]
    negative = [n for n in arr if n < 0]
    zero = [z for z in arr if z == 0]
    print(len(positive) / len(arr))
    print(len(negative) / len(arr))
    print(len(zero) / len(arr))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
