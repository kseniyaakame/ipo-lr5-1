a = input('введите строку ')
print('всего символов: ', len(a))
gl = "а, е, и, о, у, э, ю, я, ы, ё"
sogl = 'б, в, г, д, ж, з, й, к, л, м, р, н, п, c, т, ф, ч, ц, щ, ш, х,'
b = []
c = []
for i in a:
    if i in gl:
        b.append(i)
print('гласных: ', len(b))
for e in a:
    if e in sogl:
        c.append(e) 
print('согласных:', len(c))              