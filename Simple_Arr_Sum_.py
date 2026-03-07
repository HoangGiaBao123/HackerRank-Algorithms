def simpleArraySum(arr):
    total = 0
    for i in arr:
        total += i
    return total

if __name__ == '__main__':
  print(simpleArraySum([1,6,8,22,8,1,3]))
