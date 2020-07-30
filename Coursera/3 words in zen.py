import operator
from collections import Counter

zen = """
beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

zen_map = dict()

print(zen.split())
# print(len(zen.split()))
# print(type(zen.split()))
# i = 0  # counter
for word in zen.split():
	cleaned = word.strip('.,!-').lower()
	if cleaned not in zen_map:
		zen_map[cleaned] = 0  # в первый раз добавляем слово в словарь
	zen_map[cleaned] += 1
	# i += 1
# print(i)  # equals len actually
print(zen_map)

zen_items = zen_map.items()
print(zen_items)
word_count_items = sorted(
	zen_items, key=operator.itemgetter(1), reverse=True  # 1-второй индекс в тюплях; реверс, т.к. сортирует от мал. к бол.
)
print(word_count_items[:3])

# Easier way
print()

cleaned_list = [word.strip('.,!-').lower() for word in zen.split()]
# for word in zen.split():
# 	cleaned_list.append(word.strip('.,!-').lower())  # using the generator to make a list ^

print(Counter(cleaned_list).most_common(5))
