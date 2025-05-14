import java.io.*;
import java.util.*;

public class Main {
    static String board;
    static String word;
    static int[][] cache;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        cache = new int[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())];
        board = br.readLine();
        word = br.readLine();

        for (int w = word.length() - 1; w >= 0; w--) {
            for (int b = 0; b < board.length(); b++) {
                cache[b][w] = Math.max(getCache(b + 1, w + 1), getCache(b - 1, w + 1))
                        + (board.charAt(b) == word.charAt(w) ? 1 : 0);
            }
        }

        int answer = 0;
        for (int[] row : cache) {
            answer = Math.max(answer, row[0]);
        }
        System.out.println(answer);
    }

    static int getCache(int b, int w) {
        return (0 <= b && b < board.length() && 0 <= w && w < word.length())
                ? cache[b][w]
                : 0;
    }
}