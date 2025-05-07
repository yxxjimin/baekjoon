import sys


def main():
    num_btn, num_color = map(int, sys.stdin.readline().split())
    color_of = list(map(int, sys.stdin.readline().split()))

    left_to_right = [0 for _ in range(num_btn)]
    right_to_left = [0 for _ in range(num_btn)]

    for i in range(num_btn - 1):
        left_to_right[i + 1] = (
            color_of[i + 1] - color_of[i] + num_color
        ) % num_color + left_to_right[i]
        right_to_left[num_btn - i - 2] = (
            color_of[num_btn - i - 2] - color_of[num_btn - i - 1] + num_color
        ) % num_color + right_to_left[num_btn - i - 1]

    button_press_cnts = [
        max(
            left_to_right[-1] - left_to_right[i], 
            right_to_left[0] - right_to_left[i]
        ) 
        for i in range(num_btn)
    ]
    min_press_cnt = min(button_press_cnts)

    print(button_press_cnts.index(min_press_cnt) + 1)
    print(min_press_cnt)
        

if __name__ == "__main__":
    main()
