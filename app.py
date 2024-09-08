"""
#isistance - para saber se objeto é de determinado tipo
lista = [
    'a',1,1.1,True, [0,1,2],(1,2),
    {0,1},{'nome':'Luiz'},
]
for item in lista:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item, isinstance(item,set))
    elif isinstance(item, str):
        print('STR')
        item.upper()
        print(item.upper(), isinstance(item, set))
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item ,item * 2)
    else:
        print('Outro')
        print(item)
"""

"""
#Valores Trunthy e Falsy, Tipos Mutáveis e imutáveis
#Mutáveis [] {} set()
#Imutáveis () "" 0 0.0 None False range(0,10)
lista =[]
dicionario = {}
conjunto = set()
tupla =()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'
print(f'Teste', falsy('Teste'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
"""

"""
#dir, hasattr e getattr
string = 'Jorge'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe {metodo}' )
    print(string)
else:
    print(f'Não existe o método {metodo}')
"""

""""""
#Mais detalhes sobre Iterables e Iterators
#Generator expression, Iterables e Iterators
#Iterator fornece uma maneira de acessar sequencialmente os elementos de um objeto agregado semexpor sua representação subjacente.

iterable = ['Eu', 'Tenho', "__iter__"]
#iterator = iterable.__iter__() #tem o __iter__ e __next__
iterator = iter(iterable)
for iterator in iterable:
    print(iterator)
lista = [n for n in range(10)]
generator = (n for n in range(10))
print(generator)
