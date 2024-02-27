from PIL import Image

# Размер поля и начальная позиция муравья
width, height = 1024, 1024
ant_x, ant_y = 512, 512

# Начинаем с пустого белого поля
image = Image.new('1', (width, height), 1)


def invert_color(x, y):
    """Инвертируем цвет клетки."""
    value = image.getpixel((x, y))
    image.putpixel((x, y), 1 - value)


# Правила поведения муравья
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # вверх, вправо, вниз, влево
direction = 0  # начальное направление - вверх

# Основной цикл движения муравья
while 0 <= ant_x < width and 0 <= ant_y < height:
    color = image.getpixel((ant_x, ant_y))
    direction = (direction + (1 if color else -1)) % 4
    invert_color(ant_x, ant_y)
    dx, dy = directions[direction]
    ant_x += dx
    ant_y += dy

# Сохраняем изображение и считаем черные клетки
image.save('ant_path.png')
num_black_cells = sum(
                      1
                      for x in range(width)
                      for y in range(height)
                      if image.getpixel((x, y)) == 0
                      )

print(num_black_cells)
