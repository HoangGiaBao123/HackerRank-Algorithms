import os
import sys

def twoStrings(s1, s2):
    str1 = set(s1)
    str2 = set(s2)
    if any(char in str2 for char in str1):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')
    fptr.close()
