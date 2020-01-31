example_data = ["ADC", "Yes", "Debbie HAry", "David Bowie"]

#File is automatically closed at the end of the with block
with open('data.txt', 'w') as f:
    for line in example_data:
        f.write(line + "\n")