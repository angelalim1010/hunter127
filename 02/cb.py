def string_times(str, n):
  result = ""
  for i in range(n):  
    result = result + str  
  return result

def front_times(str, n):
  if len(str) < 3:
    front = str
  else:
    front = str[:3]
  result = ""
  for i in range(n):
    result += front
  return result

def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
     result = result + str[i]
  return result

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c

def string_splosion(str):
  result = ""
  for i in range(len(str)+1):
    result += str[:i]
  return result

def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars>=40:
      return True
    else:
      return False
  else:
    if cigars>=40 and cigars<=60:
      return True
    else:
      return False

def caught_speeding(speed, is_birthday):
  gift = 0
  if is_birthday:
    gift = 5
  if speed <= 60+gift:
    return 0
  elif speed >= 81+gift:
    return 2
  else:
    return 1

print (string_times('Hi',2))
print (string_times('Hi', 3))
print (string_times('Hi', 1))

print (front_times('Chocolate', 2))
print (front_times('Chocolate', 3))
print (front_times('Abc', 3))

print (string_bits('Hello'))
print (string_bits('Hi'))
print (string_bits('Heeololeo'))

print (lone_sum(1, 2, 3))
print (lone_sum(3, 2, 3)) 
print (lone_sum(3, 3, 3))

print (string_splosion('Code'))
print (string_splosion('abc')) 
print (string_splosion('ab'))

print (cigar_party(30, False))
print (cigar_party(50, False)) 
print (cigar_party(70, True))

print (caught_speeding(60, False))
print (caught_speeding(65, False)) 
print (caught_speeding(65, True))
