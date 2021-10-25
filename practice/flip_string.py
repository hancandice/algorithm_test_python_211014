S = input()


number = S[0]
count = 0

for s in S[1:]:
    if s != number:
        number = s
        count += 1

print(count//2)