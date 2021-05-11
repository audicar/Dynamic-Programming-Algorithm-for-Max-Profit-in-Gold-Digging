def disp(lines):
    for pos, each in enumerate(lines):
        for pos2, each2 in enumerate(each):
            if pos2 == m-1:
                print(each2)
            else:
                print(each2, end='  ')


file =open("test.txt","r")
lines1 = file.read().splitlines()
file.close()
lines = []
for eachline in lines1:
    lines.append(eachline.strip().split(' '))
for index1, eachline in enumerate(lines):
    for index2, eachnumber in enumerate(eachline):
        lines[index1][index2] = int(lines[index1][index2])

m = len(lines[0])
n = len(lines)

print("Input:")
disp(lines)

OPT = [ [0]*m for i in range(n)]
for i in range(0,n):
    for j in range(0,m):
        if i == 0:
            OPT[i][j] = [lines[i][j]]*3
            continue
        if j == 0:
            OPT[i][j] = [lines[i][j], max(OPT[i-1][j]) + lines[i][j], max(OPT[i-1][j+1][-2:]) + lines[i][j]]
            continue
        elif j == m-1:
            OPT[i][j] = [max(OPT[i-1][j-1][:2]) + lines[i][j], max(OPT[i-1][j]) + lines[i][j], lines[i][j]]
        else:
            OPT[i][j] = [max(OPT[i-1][j-1][:2]) + lines[i][j], max(OPT[i-1][j]) + lines[i][j], max(OPT[i-1][j+1][-2:]) + lines[i][j]]

print("Table:")
disp(OPT)
each_m_max  = []
for each_m in OPT[n-1]:
    each_m_max.append(max(each_m))

max_profit = max(each_m_max)
print("Max profit: {}".format(max_profit))
