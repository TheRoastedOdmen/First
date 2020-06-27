def append_1(iterable=[]):
	iterable.append(1)
	return iterable


print(append_1([2]))
print("defaults", append_1.__defaults__)

""" В дефолтные значения постоянно записываются переменные, 
если они ссылаются на mutable объекты, поэтому не стоит такие
объекты использовать """

print(append_1())
print(append_1())
print("defaults", append_1.__defaults__)

print(append_1())
print("defaults", append_1.__defaults__)

print('\nSolution:\n')


def function(iter=None):
	if iter is None:
		iter = []
	iter.append(1)
	return iter


#easier

"""def function (iterable = None):
	   iterable = iterable or []"""

print(function([3]))
print("defaults", function.__defaults__)

print(function())
print(function())
print("defaults", function.__defaults__)

print(function())
print("defaults", function.__defaults__)