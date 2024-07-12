# 존재하지 않는 파일을 읽기모드로 여는 경우 : FileNotFoundError 후 종료
#myFile = open('NotExist.txt', 'r')

# 잘못된 접근 : IndexError 후 종료
#myList = [1, 2, 3]
#print(myList[3])

# 예외처리 : try ~ except
try:
    myFile = open('NotExist.txt', 'r')
except FileNotFoundError as e :
    print("파일이 존재하지 않습니다." )
    print(e)

try:
    myList=[1, 2, 3]
    print(myList[3])
except IndexError as e:
    print("리스트의 인덱스가 존재하지 않습니다.")
    print(e)
    
try:
    print("Hello World")
    raise Exception ("My exception")
except Exception as e:
    print(e)
    
    