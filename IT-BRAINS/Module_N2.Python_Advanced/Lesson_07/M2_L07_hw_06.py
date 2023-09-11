# Module 2, Lecture 7, Homework 6
# Напишіть рекурсивну функцію, яка підраховує глибину
# вкладеності списків.

# Напишите рекурсивную функцию, которая является подсказкой глубины вложенных списков

# Write a recursive function that serves as a hint for the depth of nested lists.

def depth(lst):
    if isinstance(lst, list):  # Проверяем, является ли lst списком.
        max_depth = 0  # Создаем переменную max_depth,
        # которая будет содержать максимальную глубину.

        for item in lst:  # Итерируемся по элементам списка lst.
            current_depth = depth(item)   # Вызываем рекурсивно функцию depth для каждого элемента списка.
            # Это позволяет вычислить глубину каждого вложенного списка.
            max_depth = max(max_depth, current_depth)
        return max_depth + 1  # Возвращаем максимальную глубину вложенности списка плюс 1.
    else:
        # Если lst не является списком (базовый случай), то глубина вложенности равна 0.
        return 0


print("depth")
print(depth([1, [2, [3, [4, [5]]]]]))


def depth_without_recursion(lst: list) -> int:
    max_current_depth = 0  # у нас будет максимальная текущая глубина
    current_level = [(lst, 1)]

    while current_level:  # Цикл выполняется, пока current_level не станет пустым.
        next_level = []  # В этом списке мы будем хранить элементы следующего уровня обхода.
        for item, current_depth in current_level:  # Цикл for, который перебирает каждый элемент и
            # соответствующую глубину из current_level.
            # Каждый элемент будет доступен в переменной item,
            # а глубина - в переменной current_depth
            if isinstance(item, list):  # является ли item списком
                max_current_depth = max(max_current_depth, current_depth)  # Обновление переменной
                for subitem in item:  # Цикл for, который перебирает каждый подэлемент
                    # (subitem) внутри списка item.
                    next_level.append((subitem, current_depth + 1))
                    #  Добавление кортежа (subitem, current_depth + 1) в список next_level.
                    #  Кортеж содержит подэлемент и увеличенную на 1 глубину (current_depth + 1).
        current_level = next_level  # Замена значения current_level на список next_level.

    return max_current_depth


print("\ndepth_without_recursion")
print(depth_without_recursion([1, [2, [3, [4, [5]]]]]))  # 5 Пример списка depth_, для которого мы хотим вычислить
# # глубину вложенности


# depth_ = [1, [2, [3, [4, [5]]]]]

# current_level = [(depth_, 1)]
# print(current_level)

# print(depth_[0])
# print(depth_[1][0])
# print(depth_[1][1][0])
# print(depth_[1][1][1][0])
# print(depth_[1][1][1][1][0])
# print(depth_[1][1][1][1][1][0])




