def findDigits(n):
    digits = [int(d) for d in str(n) if str(d) != '0' and n % int(d) == 0]
    return len(digits)
