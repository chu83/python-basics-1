print('============== 생성 ================')
l1 = []
l2 = [1, True, 'python', 3.14]

print('============== 인덱싱 ================')
print(l2[0], l2[1], l2[2], l2[3])
print(l2[-4], l2[-3], l2[-2], l2[-1])

print('============== 반복 ================')
l3 = l2 * 2
print(l3)

print('============== 연결 ================')
l4 = l2 + [1, 2, 3]
print(l4)

print('============== 길이 ================')
print(len(l4))

print('=========== in, not in ============')
print(5 in l4)
print(5 not in l4)






