string = list(input())

for i in range(len(string) - 2, -1, -1):
    string[i] += string[i + 1]

string.sort()
for word in string:
    print(word)
