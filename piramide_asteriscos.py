
# Define el número máximo de asteriscos en la parte más ancha de la pirámide
max_stars = 7

# Genera la parte superior de la pirámide
for i in range(1, max_stars + 1, 2):
    print(f"{'*' * i:^20}")

# Genera la parte inferior de la pirámide
for i in range(max_stars - 2, 0, -2):
    print(f"{'*' * i:^20}")
