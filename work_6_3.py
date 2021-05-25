print('Введите первую статью:')
s1 = input()
print('Введите вторую статью:')
s2 = input()
print('Введите третью статью:')
s3 = input()
if len(s1) > len(s2) and len(s1) > len(s3):
    print(s1)
else:
    if len(s2) > len(s3):
        print(s2)
    else:
        print(s3)


