
try:
    data = open('data.txt', 'r').readlines()
    for line in data:
        print(line)
except FileNotFoundError as err:
    print(f"File not found: {err}")
    