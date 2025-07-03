import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static void solve(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] dp = new int[rows + 1][cols + 1];
        int maxSize = 0;

        for (int r = 1; r < rows + 1; r++) {
            for (int c = 1; c < cols + 1; c++) {
                if (grid[r - 1][c - 1] == 1) {
                    dp[r][c] = Math.min(Math.min(dp[r - 1][c - 1], dp[r][c - 1]), dp[r - 1][c]) + 1;
                    maxSize = Math.max(maxSize, dp[r][c]);
                }
            }
        }

        System.out.println(maxSize);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int rows = Integer.parseInt(st.nextToken());
            int cols = Integer.parseInt(st.nextToken());

            if (rows == 0 && cols == 0) return;

            int[][] grid = new int[rows][cols];

            for (int r = 0; r < rows; r++) {
                grid[r] = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
            }

            solve(grid);
        }
    }
}
