#coding:utf-8
#crypto numbers(50pt)

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','{','}']
number = [16,9,3,15,3,20,6,27,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,28]
flag = []

for i in number:
    flag.append(letter[int(i)-1])

print(''.join(flag))
#PICOCTF{THENUMBERSMASON}