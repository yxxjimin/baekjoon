import java.io.*;
import java.util.*;

public class Main {
    static int[][] dirs = {
            {0, 0, 1}, {0, 0, -1},
            {0, 1, 0}, {0, -1, 0},
            {1, 0, 0}, {-1, 0, 0}
    };

    static int width, height, depth;
    static boolean[][][] visited;
    static int totalCnt = 0;
    static int rottenCnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        width = Integer.parseInt(st.nextToken());
        height = Integer.parseInt(st.nextToken());
        depth = Integer.parseInt(st.nextToken());

        visited = new boolean[depth][height][width];

        Queue<int[]> queue = new LinkedList<>();

        for (int d = 0; d < depth; d++) {
            for (int r = 0; r < height; r++) {
                int[] line = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
                for (int c = 0; c < width; c++) {
                    if (line[c] == 1) {
                        totalCnt++;
                        rottenCnt++;
                        queue.add(new int[]{d, r, c});
                        visited[d][r][c] = true;
                    } else if (line[c] == 0) {
                        totalCnt++;
                    } else {
                        visited[d][r][c] = true;
                    }
                }
            }
        }

        int days = bfs(queue);
        System.out.println(totalCnt == rottenCnt ? days - 1 : -1);
    }

    static int bfs(Queue<int[]> queue) {
        int dist = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                int[] curr = queue.remove();
                int d = curr[0], r = curr[1], c = curr[2];

                for (int[] dir : dirs) {
                    int nd = d + dir[0];
                    int nr = r + dir[1];
                    int nc = c + dir[2];
                    if (isInbound(nd, nr, nc) && !visited[nd][nr][nc]) {
                        queue.add(new int[]{nd, nr, nc});
                        visited[nd][nr][nc] = true;
                        rottenCnt++;
                    }
                }
            }
            dist++;
        }

        return dist;
    }

    static boolean isInbound(int d, int r, int c) {
        return 0 <= d && d < depth &&
                0 <= r && r < height &&
                0 <= c && c < width;
    }
}
