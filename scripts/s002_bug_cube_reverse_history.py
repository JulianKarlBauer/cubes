import magiccube

cube = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
print(cube)

cube.rotate("R2 L")
print(cube.history())
print(cube)

print(cube.reverse_history())
cube.rotate(cube.reverse_history())
print(cube)
