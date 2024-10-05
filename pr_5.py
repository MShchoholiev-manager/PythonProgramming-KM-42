words = tuple(input("").split())
print(f"{", ".join(words[0:((int(len(words))) - 2)])}, {words[-2]} and {words[-1]}")