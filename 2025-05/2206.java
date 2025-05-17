import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    static int[][] grid;
    static boolean[][][] visited;

    static final int CAN_BREAK = 0;
    static final int CANNOT_BREAK = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int rows = Integer.parseInt(st.nextToken());
        int cols = Integer.parseInt(st.nextToken());
        grid = new int[rows][cols];
        visited = new boolean[2][rows][cols];

        for (int i = 0; i < rows; i++) {
            String line = br.readLine();
            for (int j = 0; j < cols; j++) {
                grid[i][j] = line.charAt(j) == '1' ? 1 : 0;
            }
        }

        System.out.println(bfs());
    }

    static int bfs() {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, CAN_BREAK});

        int dist = 0;
        while (!queue.isEmpty()) {
            dist++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.remove();
                int row = curr[0], col = curr[1], status = curr[2];

                if (row == grid.length - 1 && col == grid[0].length - 1) {
                    return dist;
                }

                for (int[] dir : dirs) {
                    int nr = row + dir[0], nc = col + dir[1];
                    if (isMovable(nr, nc, status)) {
                        queue.add(new int[]{nr, nc, status});
                        visited[status][nr][nc] = true;
                    }
                    if (isBreakable(nr, nc, status)) {
                        queue.add(new int[]{nr, nc, CANNOT_BREAK});
                        visited[CANNOT_BREAK][nr][nc] = true;
                    }
                }
            }
        }
        return -1;
    }

    static boolean isInbound(int row, int col, int status) {
        return 0 <= row && row < grid.length
                && 0 <= col && col < grid[0].length
                && !visited[status][row][col];
    }

    static boolean isMovable(int row, int col, int status) {
        return isInbound(row, col, status) && grid[row][col] == 0;
    }

    static boolean isBreakable(int row, int col, int status) {
        return isInbound(row, col, status) && grid[row][col] == 1 && status == CAN_BREAK;
    }
}