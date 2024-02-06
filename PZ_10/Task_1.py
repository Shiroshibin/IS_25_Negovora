from random import randrange

"""
                                  
Вариант 21.

В озере водится несколько видов рыб. Три рыбака поймали рыб некоторых их имеющихся
в озере видов. Определить, рыб каких видов поймал каждый рыбак и рыб каких видов,
имеющихся в озере, не выловил ни один из рыбаков.

"""



# Базовыае переменные

number_of_fisher = 3
number_of_fish = 10
all_fish = set(list(range(1, number_of_fish + 1)))
all_fisher = dict()



#  Генерируем случайных рыбоков по заданным параметрам из базовых переменных 

for i in range(1, number_of_fisher + 1):
    all_fisher[f"fisher_{i}"]: set = all_fish.copy()
    number_of_del = randrange(0, len(all_fisher[f"fisher_{i}"]) + 1)
    # print(number_of_del)
    all_fisher[f"fisher_{i}"] = list(all_fisher[f"fisher_{i}"])
    for nod in range(0, number_of_del):
        all_fisher[f"fisher_{i}"].pop(randrange(0, len(all_fisher[f"fisher_{i}"])))
    all_fisher[f"fisher_{i}"] = set(all_fisher[f"fisher_{i}"])
    
        

# Работаем с множествами

everybody_fisher_set = list(all_fisher.values())[0] 
nobody_fisher_set = all_fish 
for i in list(all_fisher.values()):
    everybody_fisher_set = everybody_fisher_set & i
    nobody_fisher_set = nobody_fisher_set - i



# Красиво выводим результат

for i in all_fisher.keys():
    print(f"{i} : {str(all_fisher[i])[1:-1] if len(all_fisher[i]) > 0 else ' '}")

print(f"Все рыбаки поймали: {str(everybody_fisher_set)[1:-1] if len(everybody_fisher_set) > 0 else ' '}")
print(f"Никто не поймал: {str(nobody_fisher_set)[1:-1] if len(nobody_fisher_set) > 0 else ' '}")



