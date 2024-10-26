def info_kwargs(**kwars):
    for key in sorted(kwars.keys()):
        print(f'{key} = {kwars[key]}')


info_kwargs(c=43, b= 32, a=32)
info_kwargs(b=3,c=2,a=1)