# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

def filter_list(lst):
    lst = list(filter(lambda x: isinstance(x, str), lst))
    print(lst)

lst_ch = ['st1', 'asb', 2, 5, 'w', 4.0, 'one', 'ав']
filter_list(lst_ch)
