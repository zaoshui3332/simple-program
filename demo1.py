# n = input("Enter:")
# n = int(n)
# if n% 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# n = input("Enter:")
# n = int(n)
# if n >= 0:
#     print(n)
# else:
#     print(-n)



#2-1-3
# a = input("a=")
# b = input("b=")
# a = float(a)
# b = float(b)
# if a>b :
#     c=a
# else:
#     c=b
# print(c)



# m = input("Enter make:")
# m = float(m)
# if m<0 or m>100 :
#     print("Invalid")
# elif m>=90 :
#     print("A")
# elif m>=80 :
#     print("B")
# elif m>=70 :
#     print("C")
# elif m>=60 :
#     print("D")
# elif m>=50 :
#     print("E")



# w=input("w=")
# w=int(w)
# if w==0:
#     s="Sunday"
# elif w==1:
#     s="Sunday"
# elif w==2:
#     s="Monday"
# elif w==3:
#     s="Tuesday"
# elif w==4:
#     s="wednesday"
# elif w==5:
#     s="Thursday"
# elif w==6:
#     s="Friday"
# elif w==7:
#     s="Saturday"
# else:
#     s="Unknown"
# print(s)



# import math
# c=input("c=")
# a=input("a=")
# b=input("b=")
# a=float(a)
# b=float(b)
# c=float(c)
# if a!=0:
#     d=b*b-4*a*c
#     if d>0:
#         d=math.sqrt(d)
#         x1=(-b+d)/2/a
#         x2=(-b-d)/2/a
#         print("x1=",x1,"x2=",x2)
#     elif d==0:
#         print("x1,x2=",-b/2/a)
#     else:
#         print("无实数解")
# else:
#     print("不是一元二次方程")




# def max(x,y):
#     m=x
#     if y>x:
#         m=y
#         return m
#     a=input("a=")
#     b=input("b=")
#     c=input("c=")
#     a=float(a)
#     b=float(b)
#     c=float(c)
#     d=max(a,b)
#     c=max(d,c)
#     print("max=",c)


# print("hello world!")



# from numpy.core.defchararray import lower, upper
# print("输入quit退出程序")
# while True:
#     a=input()
#     if a.lower()=='quit':
#         print("程序结束")
#         break
#     else:
#         if a.isalpha():
#             b = lower(a)
#             c = upper(a)
#             if a == b:
#                 print("输入的字母为小写")
#             else:
#                 if a==c:
#                     print("大写")
#                 else:
#                     print("大小混写")
#
#         else:
#             print("请输入正确的英文字母")



print('nf')
while True:
    a=int(input())
    if a==99999:
        print('t')
        break
    else:
            b=a//4
            if b==0:
                print("r")
            else:
                print("p")




