import bisect
import pathlib
import re


ROOT_DIR = pathlib.Path(__file__).parent
FILE_PATH = ROOT_DIR / 'README.md'
STEP_SIZE = 2000


def _depth_first() -> dict[int, pathlib.Path]:
    stack = [ROOT_DIR]
    problem_map = dict()
    
    while stack:
        curr_dir = stack.pop()
        for subpath in curr_dir.iterdir():
            if subpath.is_dir():
                stack.append(subpath)
            elif matched := re.findall(r'boj-(\d+).*', str(subpath)):
                number = int(matched[0])
                rel_path = subpath.relative_to(ROOT_DIR)
                problem_map[number] = rel_path
    
    return problem_map


def _compose_data(
    data: dict[int, pathlib.Path]
) -> dict[int, list[tuple[int, pathlib.Path]]]:
    max_number = max(data.keys())
    last_index = max_number // STEP_SIZE + 1

    new_keys = [i * STEP_SIZE for i in range(last_index)]
    new_data = {k: [] for k in new_keys}

    for num, path in data.items():
        key = new_keys[bisect.bisect_right(new_keys, num) - 1]
        new_data[key].append((num, path))

    return {k: sorted(v) for k, v in new_data.items()}


def _markdown_heading(n: int, title: str) -> str:
    return f'{"#" * n} {title}\n'


def _markdown_table(
    data: dict[int, list[tuple[int, pathlib.Path]]]
) -> str:
    th = '|문제 번호|기록|\n|-|-|\n'
    
    for key, val in data.items():
        link_str = [f'[{num}]({str(path)})' for num, path in val]
        td = f'|{key}|{" ".join(link_str)}|\n'
        th += td

    return th


def _markdown_content() -> str:
    return '\n'.join([
        _markdown_heading(1, '알고리즘'),
        _markdown_heading(3, 'Baekjoon'),
        _markdown_table(
            _compose_data(
                _depth_first()
            )
        )
    ])


if __name__ == '__main__':
    with open(FILE_PATH, 'w') as f:
        f.write(_markdown_content())
