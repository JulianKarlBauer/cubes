import magiccube

print("Start with solved cube")
cube = magiccube.Cube(
    2,
    "".join(4 * letter for letter in "YRGOBW"),
)
print(cube)


print("Check that cube is solved")
print(f"cube.is_done() = {cube.is_done()}")

##################

rotations = "R' L2 U R' L"

print(f"cube.rotate({rotations})")
cube.rotate(rotations)
print(cube)
print(f"cube.history()= {cube.history()}")

print(f"cube.reverse_history(to_str=True) = {cube.reverse_history(to_str=True)}")

print(f"cube.rotate(cube.reverse_history())")
cube.rotate(cube.reverse_history())
print(cube)

##################

print(f"cube.is_done()={cube.is_done()}")
