def reverse_text(text):
    for ch in reversed(text):
        yield ch


for char in reverse_text("step"):
    print(char, end='')
