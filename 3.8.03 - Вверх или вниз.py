def make_strings_big(*args, reverse=False):
    for arg in args:
        if reverse:
            print(arg.lower(), end='\n')
        else:
            print(arg.upper(), end='\n')


make_strings_big('У лукоморья дуб зелёный',
                 'Златая цепь на дубе том:',
                 'И днём и ночью кот учёный', reverse = True)