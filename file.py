import math

def median(input):
  if (len(input) % 2):
    return input[math.floor(len(input) / 2)]
  else:
    return (input[math.floor(len(input) / 2)] + input[math.floor((len(input) / 2) + 1)]) / 2
