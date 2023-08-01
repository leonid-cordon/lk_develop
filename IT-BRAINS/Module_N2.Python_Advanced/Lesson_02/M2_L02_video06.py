age = input()

try:
    age = int(age)   # пишем только то что может дать ошибку
    print(age)
    print("Success")
except Exception as e:
    print("Exception")
    age = 18
else:
    print('Success')    # а те что не дают ошибки пишем сюда
                        # явно лучше чем неявное

