# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.


lst = [1,1,1,2,3,3,4,4,5,5,6,6,7,8,9]

res_lst = []

for i in lst:
    if lst.count(i) > 1 and i not in res_lst:
        res_lst.append(i)

print(*res_lst)

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

article = "Германское командование ещё с марта 1915 года готовило крупную операцию по прорыву вражеского фронта с применением химического оружия. " \
          "В предстоящем наступлении немцы планировали применить химическую газобаллонную атаку. Удар наносился на участке стыка 2-й английской армии " \
          "и 20-го французского корпуса. В течение нескольких дней германские химические войска ночью установили 150 газобаллонных батарей. 22 апреля " \
          "на позиции британских войск было выпущено 180 тонн хлора. Желтовато-зелёное облако двинулось на позиции противника, за ним в марлевых " \
          "повязках наступала германская пехота. Английские солдаты, не будучи снабжены средствами защиты от газа, задыхались и падали замертво. " \
          "Англичане в панике оставляли свои позиции, которые без боя занимали германские солдаты. Однако, по некоторым данным, германское командование " \
          "не учло погодные условия, и часть хлора была ветром отнесена к позициям германских войск, в результате чего те, кто не был в защитной маске," \
          " также получили отравление (правда, о смертельных случаях данных нет). От хлора пострадало 15 000 человек, 5000 из которых умерли. " \
          "Между английскими и французскими войсками образовался разрыв в 3,5 км. Дорога на Ипр оказалась свободна. Однако, не имея резервов, " \
          "германское командование не смогло извлечь выгоды из сложившейся ситуации. На автомашинах и пешим порядком англичане и французы подтянули " \
          "резервы и заняли брешь в обороне, все последующие попытки германских войск прорвать оборону оказались безуспешными. Англичане и французы " \
          "уже были оснащены простейшими средствами защиты от химического оружия. В дальнейших боях в мае немцам удалось продвинуться на " \
          "незначительное расстояние, но главная задача — прорыв фронта и захват Ипра — выполнена не была. Первое в истории применение газа принесло" \
          " германцам ограниченный успех, однако оно явилось началом массового применения химических средств борьбы воюющими государствами. " \
          "Развивались средства защиты и новый элемент боевого обеспечения — противохимическая защита войск. Уже в 1915 году простейшие " \
          "марлевые повязки были заменены противогазами."

article = article.lower().split()

words = {}
article_list = [''.join(filter(str.isalpha, i)) for i in article]

while "" in article_list:
    article_list.remove('')

for word in article_list:
    words.setdefault(word, article_list.count(word))

count_word = 1
while count_word <= 10:
    count_word += 1
    maximum = max(words, key=words.get)
    print(f'{maximum:>5} = {words[maximum]}')
    words.pop(maximum)

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака

from operator import itemgetter


travel_voc = {'нож': 1, 'котелок': 1, 'палатка': 7, 'спальник': 2, 'еда': 8, 'книги': 4, 'гитара': 6}

backpack = 21
item_weight = 0
backpack_weight = 0

for things, value in dict(sorted(travel_voc.items(), key=itemgetter(1))).items():
    item_weight += travel_voc[things]

    if item_weight <= backpack:
        print(things, '=', value)
        backpack_weight += travel_voc[things]

print("Вес рюкзака с вещами: ", backpack_weight)
