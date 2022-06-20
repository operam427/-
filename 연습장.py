# <연습장>

def midex(*score):
  average = sum(score) / len(score)
  return("{:.2f}".format(average))

print(midex(82, 39, 90, 40, 20, 89, 69, 79, 89, 98, 79, 88, 38, 58, 68, 80,
              78, 73, 89, 93))

a = (82, 39, 90, 40, 20, 89, 69, 79, 89, 98, 79, 88, 38, 58, 68, 80,
              78, 73, 89, 93)

print(sum(a))
print(len(a))
print(sum(a)/len(a))

def midexam(*num):
  return sum(num) / len(num)

print(midexam(82, 39, 90, 40, 20, 89, 69, 79, 89, 98, 79, 88, 38, 58, 68, 80, 78, 73, 89, 93))