from PIL import Image
import matplotlib.pyplot as plt

# Substitua pelos caminhos corretos das suas imagens
image_paths = [
    "6 abre (1) - Foto Carlos Moura_Agência Senado.jpg",
    "6 abre (2) - Foto Edilson Rodrigues_Agência Senado.jpg",
    "6 abre (3) - Foto Waldemir Barreto_Agência Senado.webp"
]

# Abrir as imagens
images = [Image.open(path) for path in image_paths]

# Redimensionar todas para a mesma altura
target_height = 400
resized_images = []

for img in images:
    aspect_ratio = img.width / img.height
    new_width = int(target_height * aspect_ratio)
    resized_images.append(img.resize((new_width, target_height)))

# Calcular largura total
total_width = sum(img.width for img in resized_images)

# Criar imagem final
collage = Image.new('RGB', (total_width, target_height))

# Colar as imagens
x_offset = 0
for img in resized_images:
    collage.paste(img, (x_offset, 0))
    x_offset += img.width

# Mostrar a colagem
plt.figure(figsize=(12, 6))
plt.imshow(collage)
plt.axis('off')
plt.tight_layout()
plt.show()

# Salvar a colagem
collage.save("colagem_senadores.jpg")
