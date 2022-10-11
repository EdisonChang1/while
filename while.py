#以下的題目 只會用到while 和計算式
"""1.)
透過while
印出
1
2
3
4
"""
print("1")
x=1
while x<=4:
    print(x)
    x=x+1
"""
2.)
透過while
印出
5
4
3
2
1
"""
print("2.")
x=5                #設定5為一開始迴圈數字
while x>=1:        #設定迴圈結束最後的數字
    print(x)       #執行結果
    x=x-1          #每次進入迴圈增加或減少的數值
"""
3.)
透過while
印出
50
30
10
0
"""
print("3.")
x=50
while x>=0:
    if x!=40:
        if x!=20:
            print(x)
    x=x-10
"""
4.)
透過while 把 1+2+3+4的答案10算出來

印出
10
"""
print("4.")
x=1
str=0                       #str=總計值
while x<5:
    str=str+x
    x=x+1
print(str)
"""
5.)
透過while 把以下的答案印出來

印出
0
1
3
6
10

"""
print("5.")
total=0
x=0
while x<5:
    total=total+x
    print(total)
    x=x+1
"""
6.)
透過while 把 1*2*3*4的答案24算出來

印出
24
"""
print("6.")
total = 1
x = 1
while x <= 4:
    total=total*x
    x=x+1
print(total)
"""
7.)
透過while 把 10000/5/4/3/2/1的答案算出來

印出
83.33
"""
print("7.")
total = 10000
x = 5
while x >0:
    total = total/x
    x = x - 1

print(total)
"""
8.)
透過while
印出

     B
   BBB
BBBBB

"""
print("8.")
str1=""   #處理空白
str2=""
x=0
while x<3:
    str1=("B"*(x*2+1))                 #B重複幾次
    #print(str1)
    str2=(" "*(2-x))                     #空白  重複幾次
    #print("["+str2+"]")
    print(str2+str1)
    x=x+1
"""
9.)  
透過while
印出
A
BB
CCC
DDDD
EEEEE
"""
print("9.")
list1=["A","B","C","D","E"]
x=0
while x<5:
    str1=list1[x]            #總共5行
    str2=""
    y=0
    while y<=x:
        str2=str1+str2
        y=y+1
    print(str2)
    x=x+1
"""
10.)  
透過while 計算出 254  的二進位為多少
印出
"""
print("10.")
str1=""
x=254
while x>0:
    y=str(x%2)
    str1=y+str1
    x=x//2
print(str1)














