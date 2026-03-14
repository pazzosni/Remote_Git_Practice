#A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다. for문을 사용하여 A학급의 평균 점수를 구해보자.
#[ 70, 60, 55, 75, 95, 90, 80, 80, 85, 100 ]
A = [70,60,55,75,95,90,80,80,85,100]
total = 0

for score in A:
  total += score #your code here
average = total / len(A)#코드 값이 몇개가 오든 받아줄 수 있음
print(average)