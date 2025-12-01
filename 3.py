from PIL import Image
import random

filename = "example.jpg"
image = Image.open(filename)
pixels = image.load()
width, height = image.size
depth = len(image.getbands())
img_type = image.format

print(f"Ширина: {width}")
print(f"Высота: {height}")
print(f"Глубина: {depth}")
print(f"Формат: {img_type}")

while True:
    choice = input("Выбрать эффект(1)   Сохранить(2) ")

    if choice == "1":
        print("Выберите эффект:")
        print("1 — Черно-белое")
        print("2 — Закрасить случайный квадрат")
        print("3 — Добавить шум")

        effect = input("Введите номер эффекта: ")

        if effect == "1":
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y][:3]
                    gray = (r + g + b) // 3
                    pixels[x, y] = (gray, gray, gray)
            print("Эффект применён: черно-белое")

        elif effect == "2":
            colors = {
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "blue": (0, 0, 255),
                "white": (255, 255, 255),
                "black": (0, 0, 0)
            }

            print("Доступные цвета:", ", ".join(colors.keys()))
            chosen = input("Введите цвет: ")

            if chosen not in colors:
                print("Нет такого цвета.")
                continue

            color = colors[chosen]
            square_size = min(width, height) // 4
            start_x = random.randint(0, width - square_size)
            start_y = random.randint(0, height - square_size)

            for y in range(start_y, start_y + square_size):
                for x in range(start_x, start_x + square_size):
                    pixels[x, y] = color

            print("Эффект применён: случайный квадрат закрашен")

        elif effect == "3":
            num_noise_pixels = (width * height) // 10

            for _ in range(num_noise_pixels):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                pixels[x, y] = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            print("Эффект применён: добавлен шум (10%)")

        else:
            print("Нет такого эффекта.")
            continue

    if choice == "2":
        while True:
            save_name = input("Введите имя для сохранения (например, result.png): ")
            try:
                image.save(save_name)
                print(f"Изображение сохранено как {save_name}")
                quit()
            except Exception as e:
                print("Ошибка сохранения:", e)
                print("Попробуйте другое имя.\n")


