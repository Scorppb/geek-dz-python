# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text_my = 'Напишите программуабв, удаляющуюабв из текста все словаабв, содержащие "абв"'
text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
my = " ".join(text_my)
print(text_my)
print(my)
