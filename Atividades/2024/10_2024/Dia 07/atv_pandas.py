import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print(f'\n--------------------------- Versão ---------------------------\n{pd.__version__}')
print(f'\n--------------------------- Tabela ---------------------------\n{df.head(12)}')
print(f'\n--------------------------- Info ---------------------------\n{df.info()}')
df.set_index('PassengerId', inplace=True)
print(f'\n--------------------------- Tabela ---------------------------\n{df.head(12)}')
print(f'\n--------------------------- Colunas ---------------------------\n{df.columns}')
print(f'\n--------------------------- Valores ---------------------------\n{df.values}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.loc[1]}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.loc[[1,2],['Name','Sex','Age']]}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.loc[10:20]}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.loc[10:30:2]}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.loc[1:10,['Name','Sex','Age']]}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.query('Age > 20').head()}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.query('Age > 20')}')
print(f'\n--------------------------- Selecionar ---------------------------\n{df.query('Age > 20 & Sex=="male"').head()}') # & = and, | = or
df.to_csv('dataset.csv', sep='.', index=False, encoding='utf-8-sig') # Salvar
    
print('''
=-------------------------- 01 --------------------------=
- Quantas crianças abaixo de 10 anos sobreviveram?
''')
num1 = df.query('Age < 10')
print(f'R: {num1.count()['Survived']}')
# num1.to_csv('num1.csv', sep='.', index=False, encoding='utf-8-sig')

print('''
=-------------------------- 02 --------------------------=
- Quantas mulheres sobreviveram?
''')

num2 = df.query('Sex=="female"')
print(f'R: {num2.count()['Survived']}')
# num2.to_csv('num2.csv', sep='.', index=False, encoding='utf-8-sig')

print('''
=-------------------------- 03 --------------------------=
03. Quantos homens sobreviveram?
''')
num3 = df.query('Sex=="male"')
print(f'R: {num3.count()['Survived']}')
# num3.to_csv('num3.csv', sep='.', index=False, encoding='utf-8-sig')

print('''
=-------------------------- 04 --------------------------=
- Quantos idosos de 50 anos sobreviveram?
''')
num4 = df.query('Age > 50')
print(f'R: {num4.count()['Survived']}')
# num4.to_csv('num4.csv', sep='.', index=False, encoding='utf-8-sig')

print('''
=-------------------------- 05 --------------------------=
- Quantas crianças abaixo de 12 anos do sexo feminino sobreviveram?
''')
num5 = df.query('Age < 12 & Sex=="female"')
print(f'R: {num5.count()['Survived']}')
# num5.to_csv('num5.csv', sep='.', index=False, encoding='utf-8-sig')