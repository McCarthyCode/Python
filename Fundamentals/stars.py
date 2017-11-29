def stars(l):
    for i in l:
        string = ""
        if isinstance(i, int):
            for j in range(i):
                string += "*"
        elif isinstance(i, str):
            for j in range(len(i)):
                string += i[0].lower()
        print string

x = [4, 6, 1, 3, 5, 7, 25]
stars(x)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)