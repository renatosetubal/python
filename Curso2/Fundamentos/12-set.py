filme = {"O Alto da compadecida","Bad Boys","Bad Boys 2", "Formigas","Carros","Independence Day"}

print(type(filme))
print(len(filme))
exemploSet={"Inception", True, 1, 8.7}
print(exemploSet)
filme.update(exemploSet)
print(filme)
filme.remove(True)
filme.remove("Formigas")
print(filme)