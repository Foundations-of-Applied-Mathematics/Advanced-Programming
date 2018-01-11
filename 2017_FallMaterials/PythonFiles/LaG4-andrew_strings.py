#String splitting

a = ['1234','1234','1234','1234']

print(a)

for i in range(len(a)):
	for j in range(len(a)):
		if a[i][j] == '3':
			# a[i][j] = 'X' #STRINGS ARE IMMUATBLE
			a[i] = a[i][:j] + 'X' + a[i][j+1:]

print(a)

a = ['cat', 'cat fish', 'dogs and cats are animals', 'tigers and bears']


print([x for x in a if x.startswith('cat')]) #also endswith

print([x for x in a if 'cat' in x]) #contains
print([x for x in a if 'cat' not in x])


print([x.index('cat') for x in a if 'cat' in x]) #breaks

print([x.find('cat') for x in a]) #gives -1

print([x.upper() for x in a])
print([x.capitalize() for x in a])


new = [x.capitalize() for x in a]

print([[x.isupper() for x in s] for s in new]) #double looping

#isalpha, isnum, isdigit, istitle, isspace

print([x.swapcase() for x in new]) #funny example
