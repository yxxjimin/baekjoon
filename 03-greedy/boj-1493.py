# Read input
length, width, height = map(int, input().split())
target_volume = length * width * height

n = int(input())
cubes = []
for _ in range(n):
    cubes.append(tuple(map(int, input().split())))
cubes.sort(reverse=True)

total_cubes = 0
aggregated_volume = 0
for cube in cubes:
    length_exp, cube_count = cube
    cube_length = 2 ** length_exp
    cube_volume = cube_length ** 3
    
    # Largest volume with current cube size
    current_max_volume = (cube_volume * (length // cube_length) 
                          * (width // cube_length) * (height // cube_length))

    # Constructable volume with current cube count
    constructed_volume = min(
        current_max_volume - aggregated_volume, cube_volume * cube_count)
    
    aggregated_volume += constructed_volume
    total_cubes += int(constructed_volume / cube_volume)

if (aggregated_volume == target_volume):
    print(total_cubes)
else:
    print(-1)
