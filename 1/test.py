mas = raw_input().split()
res = 'NO' if abs(int(mas[2])-int(mas[4])) == abs(int(mas[3])-int(mas[5])) else 'YES'
print(res)

