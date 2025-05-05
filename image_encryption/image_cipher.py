from PIL import Image

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGBA")
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b, a = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256,
                a
            )

    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGBA")
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b, a = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256,
                a
            )

    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")
