import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[][] values;
    static int[][] maxVals;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int rows = Integer.parseInt(st.nextToken());
        int cols = Integer.parseInt(st.nextToken());

        values = new int[rows][cols];
        maxVals = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < cols; j++) {
                values[i][j] = Integer.parseInt(st.nextToken());
                maxVals[i][j] = Integer.MIN_VALUE;
            }
        }

        for (int i = 0; i < rows; i++) {
            if (i == 0) {
                maxVals[i][0] = values[i][0];
                for (int j = 1; j < cols; j++) {
                    maxVals[i][j] = maxVals[i][j - 1] + values[i][j];
                }
                continue;
            }

            int[] leftToRight = new int[cols];
            leftToRight[0] = maxVals[i - 1][0] + values[i][0];
            for (int j = 1; j < cols; j++) {
                leftToRight[j] = Math.max(maxVals[i - 1][j], leftToRight[j - 1]) + values[i][j];
            }

            int[] rightToLeft = new int[cols];
            rightToLeft[cols - 1] = maxVals[i - 1][cols - 1] + values[i][cols - 1];
            for (int j = cols - 2; j >= 0; j--) {
                rightToLeft[j] = Math.max(maxVals[i - 1][j], rightToLeft[j + 1]) + values[i][j];
            }

            for (int j = 0; j < cols; j++) {
                maxVals[i][j] = Math.max(leftToRight[j], rightToLeft[j]);
            }
        }

        System.out.println(maxVals[rows - 1][cols - 1]);
    }
}
