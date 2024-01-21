def get_stars(n):
    if n == 1:
        return ["*"]
    elif n == 2:
        return [
            "*****",
            "*    ",
            "* ***",
            "* * *",
            "* * *",
            "*   *",
            "*****"
        ]
    
    previous_stars = get_stars(n - 1)
    previous_width = len(previous_stars[0])
    new_stars = (
        ["*" * (previous_width + 4), 
         "*" + " " * (previous_width + 3)]
        + ["* " + line + " *" for line in previous_stars]
        + ["*" + " " * (previous_width + 2) + "*", 
           "*" * (previous_width + 4)]
    )
    new_stars[2] = new_stars[2][:-2] + "*" + new_stars[2][-1]
    
    return new_stars

n = int(input())
for line in get_stars(n):
    print(line.strip())
