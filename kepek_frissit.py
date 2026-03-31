import os
import json

# Kepek keresese az img mappakban
img_exts = ('.jpg', '.jpeg', '.png', '.webp')
result = {}

for i in range(1, 13):
    folder = os.path.join('img', str(i))
    if os.path.isdir(folder):
        files = sorted([
            f for f in os.listdir(folder)
            if f.lower().endswith(img_exts)
        ])
        result[str(i)] = [f'img/{i}/{f}' for f in files]
        print(f'img/{i}/ : {len(files)} kep talaltva -> {files}')
    else:
        result[str(i)] = []
        print(f'img/{i}/ : mappa nem letezik')

# Mentes
with open('images.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('\nKesz! images.json frissitve.')
input('Nyomj ENTER-t a bezarashoz...')