import magiccube

print("Start with solved cube")
cube = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
print(cube)

print("Check that cube is solved")
print(f"cube.is_done() = {cube.is_done()}")

##################

rotations = "R' L2 U D' F B'2 R' L"
print(f"cube.rotate({rotations})")
cube.rotate(rotations)
print(cube)

print("cube.scramble()")
print(cube)

print(f"cube.history() = {cube.history()}")

print("cube.reset()")
cube.reset()
print(cube)

print(f"cube.history() = {cube.history()}")

##################

print(f"cube.rotate({rotations})")
cube.rotate(rotations)
print(cube)
print(f"cube.history()= {cube.history()}")

print(f"cube.reverse_history(to_str=True) = {cube.reverse_history(to_str=True)}")

print(f"cube.rotate(cube.reverse_history(to_str=True))")
cube.rotate(cube.reverse_history())
# cube.rotate("L' R B2 F' D U' L'2 R")
print(cube)
