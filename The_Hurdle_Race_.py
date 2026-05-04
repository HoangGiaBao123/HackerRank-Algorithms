import os

def hurdleRace(k, height):
    highest_hurdle = max(height)
    if highest_hurdle <= k:
        return 0
    return highest_hurdle - k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
    fptr.write(str(result) + '\n')
    fptr.close()
