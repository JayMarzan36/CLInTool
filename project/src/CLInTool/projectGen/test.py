dictionary = {'test1' : {'test3' : ['test5']}, 'test2' : {'test4' : 'test6'}}

get1 = dictionary.get('test1', {})
print(get1.get('test3', {}))

get2 = get1.get('test3', {})
print(get2[0])