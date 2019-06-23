# coding:utf-8
import codecs
import re
#入力した値を2進数、16進数、8進数として扱い、ASCIIデコードする

# 1問目。01100100 01101111 01100011 01110100 01101111 01110010
print("input decimal numbers")
a = map(str, input().split())
for i in a:
    print(chr(int(i,2)),end="")
    #doctor

print('\n')

# 2問目。73746f7665
print("input hex numbers")
b = str(input())
b_slice = re.split('(..)',b)[1::2]
print(b_slice)
for i in b_slice:
    print(chr(int(i,16)), end="")
    # stove

print('\n')

# 3問目　164 151 155 145
print("input octal numbers")
c = map(str, input().split())
for i in c:
    print(chr(int(i,8)),end="")
    # time

print('\n')
