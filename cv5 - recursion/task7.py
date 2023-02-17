def transfer(z, s, do):
  print(f"Transfer disk from {z} to {s}")
  print(f"Transfer disk from {s} to {do}")

def tower_of_hanoi(num_of_discs, z, tmp, to):
  if num_of_discs == 0:
    return
  tower_of_hanoi(num_of_discs - 1, z, to, tmp)
  print(f"Transfer disk from {z} to {to}")
  tower_of_hanoi(num_of_discs - 1, tmp, z, to)

tower_of_hanoi(4, "A", "B", "C")