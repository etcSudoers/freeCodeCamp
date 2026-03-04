def count_perfect_cubes(a, b):
    # Determine the start and end points
    start = min(a, b)
    end = max(a, b)
    counter = 0
    for i in range(start, end + 1):
        if i < 0:
            i = abs(i)
        # Calculate the cube root and round it
        cube_root = round(i ** (1 / 3))
        # Check if the cube of the rounded root equals the original number
        if cube_root ** 3 == i:
            print(f"Perfect cube for number {i} being {cube_root}")
            counter += 1
    return counter


print(count_perfect_cubes(3, 30)) #should return 2.
print(count_perfect_cubes(1, 30)) #should return 3.
print(count_perfect_cubes(30, 0)) #should return 4.
print(count_perfect_cubes(-64, 64)) #should return 9.
print(count_perfect_cubes(9214, -8127)) #should return 41.