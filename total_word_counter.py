import codecs

file = codecs.open('/home/vlad/Downloads/ViM.txt', 'r', 'cp1251')
text = file.read()

def split_text(text):
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('Наташи', 'Наташа')
    text = text.replace('Наташе', 'Наташа')
    text = text.replace('Наташу', 'Наташа')
    text = text.replace('Наташей', 'Наташа')
    text = text.replace('Пьера', 'Пьер')
    text = text.replace('Пьеру', 'Пьер')
    text = text.replace('Пьером', 'Пьер')
    text = text.replace('Пьере', 'Пьер')
    value = text.split()
    return value

global_counter = 0
for sentence in text.split('.'):
    pier_count = 0
    nat_count = 0
    for word in split_text(sentence):
        if word == 'Наташа':
            nat_count = nat_count + 1
        elif word == 'Пьер':
            pier_count = pier_count + 1

    if nat_count >= 1 and pier_count >=1:
        global_counter += 1

print (global_counter)

file.close()
