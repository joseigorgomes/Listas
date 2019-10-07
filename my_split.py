def my_split(text, sep):
    help = ''
    split = []

    for e in text:
        if e != sep:
            help += e
        elif help != '':
            split.append(help)
            help = ''
    if help != '':
        split.append(help)
    return split

text = input()
sep = ' '
my_split = my_split(text, sep)
print(my_split)
