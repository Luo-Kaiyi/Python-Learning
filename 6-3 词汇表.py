dictionary = {
    'if': "表条件判断",
    'while': "表示循环条件",
    'switch': '表条件选择',
    'output': '输出',
    'input': '输入',
}
for key in dictionary.keys():
    print(key)
for value in dictionary.values():
    print(value)

dictionary['print'] = 'python输出'
dictionary['len'] = 'python中长度'
dictionary['main'] = '主程序（函数）'

for key,value in dictionary.items():
    print(key + ": " + value)