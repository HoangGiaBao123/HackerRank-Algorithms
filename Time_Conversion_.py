def timeConversion(s):
    time_format = s[-2:]
    time_str = s[:-2].split(':')
    if time_format == "PM":
      if 1 <= int(time_str[0]) <= 11:
        time_str[0] = str(int(time_str[0]) + 12)
    elif time_format == "AM":
        if time_str[0] == "12":
            time_str[0] = "00"
    return ":".join(time_str)
