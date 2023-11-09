# Enter your code here. Read input from STDIN. Print output to STDOUT
word = str(input())
for i in len(word):
    print(list(tuple(word[i],word[i+1])))