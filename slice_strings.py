
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = []
T = int(input())
lists = []
# lis2 = []
str_s1 = ''
str_s2 = ''

# read input with length string
for s in range(0, T):
    S.append(input())

for i in range(T):
    for j in range(len(S[i])):
        if 1 <= T and T <= 10:
            if 2 <= len(S) and len(S) <= 10000:
                if j % 2 == 0:
                    str_s1 += (S[i][j])
                else:
                    str_s2 += (S[i][j]) 
    #print(str_s1 + ' '+ str_s2)
    lists.append(str_s1 + ' '+ str_s2)
    str_s1 = ''
    str_s2 = ''

for l in lists:
    print(l)