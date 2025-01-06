import collections
import pathlib
import re


type ProblemFilesMap = dict[int, list[pathlib.Path]]
type GroupedProblemFilesMap = dict[int, list[tuple[int, pathlib.Path]]]


def _find_all_files(root: pathlib.Path) -> ProblemFilesMap:
    stack = [root]
    problem_map = collections.defaultdict(list)
    
    while stack:
        curr_dir = stack.pop()
        for subpath in curr_dir.iterdir():
            if subpath.is_dir():
                stack.append(subpath)
            elif matched := re.findall(r'boj-(\d+).*', str(subpath)):
                number = int(matched[0])
                rel_path = subpath.relative_to(root)
                problem_map[number].append(rel_path)
    
    return problem_map


def _aggregate_problem_files(
    data: ProblemFilesMap, 
    step_size: int
) -> GroupedProblemFilesMap:
    aggregated_map = collections.defaultdict(list)

    for key, values in data.items():
        new_key = (key // step_size) * step_size
        for value in values:
            aggregated_map[new_key].append((key, value))

    return dict(
        sorted({k: sorted(v) for k, v in aggregated_map.items()}.items())
    )


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


if __name__ == '__main__':
    ROOT_DIR = pathlib.Path(__file__).parent
    FILE_PATH = ROOT_DIR / 'README.md'
    STEP_SIZE = 2000

    with open(FILE_PATH, 'w') as f:
        f.write(
            '\n'.join([
                _markdown_heading(1, '알고리즘'),
                _markdown_heading(3, 'Baekjoon'),
                _markdown_table(
                    _aggregate_problem_files(
                        data=_find_all_files(ROOT_DIR),
                        step_size=STEP_SIZE
                    )
                )
            ])
        )
