#기타 연산자1
var=[1,2,3]
print(1 in var)

var=["chris","tommy","harry"]
print("chris" in var)

var="Hello Python"
print("J" not in var)

#조건부 표현식
var=10
var="Big" if 0<var else "Small"
print(var)

#while문
cond=0
while cond<10:
    cond=cond+1
    if cond%3==0 : continue
    if cond%5==0 : break
print(cond)

#for문
var=[1,2,3]
for one in var:
 print(one)
    
var=[(1,1),(2,2),(3,3)]
for(first,second) in var:
    print(first+second)
    
sum=0
var=range(1,10)
for one in var:
    sum=sum+one
print(sum)

#함수코드 예
def add(x, y):
    print(x)
    print(y)
    return x + y
val_x=1
val_y=2
val_sum=add(val_x,val_y)
print(val_sum)

#매개변수 개수 정의 어려운 경우
def sum(*values):
    result=0
    for one in values:
        result=result+one
        return result
result=sum(1,2,3)
print(result)

#2개값을 반환화는 함수
def calc(a,b):
    return a+b, a*b

result=calc(1,3)
print(result)

result1,result2=calc(3,3)
print(result1)
print(result2)

#매개변수에 초기값을 설정하는 경우
def calc(a,b=10):
    return a+b, a*b

result=calc(1,3)
print(result)

result=calc(10)
print(result)

#매개변수에 이름 짓는 경우
def cal(a,b):
    return a+b, a-b

result=calc(b=3,a=1)
print(result)

#파이썬 함수의 변수 범위
val=0
def processing(data):
    global val
    val=data
    data=data*10
    return data*data

data=10
result=processing(data)
print(val)
print(data)
print(result)