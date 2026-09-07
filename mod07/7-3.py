while True:
    galloona = int(input("Anna määrä galloonoina niin muunnan ne litroiksi:\n"))
    if galloona < 0:
        break
    def f(galloona):
        return galloona * 3.785
    print(f(galloona))