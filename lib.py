
class Lib():
    def open_input(day, test=False):
    m = []
    path = f"inputs/d{day}"
    if test: path + "_test"
    with open(path + ".txt") as f:
        while l:= f.readline():
            m.append(list(l.strip()))
    return m