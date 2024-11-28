import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Title: 백준 4848번
 */
public class Main {
    private String[] cache = new String[16];

    private int parse(String str) {
        int cnt = 0;
        int stack = 0;
        for (int i = 1; i < str.length() - 1; i++) {
            if (str.charAt(i) == '{') {
                stack++;
            } else if (str.charAt(i) == '}') {
                stack--;
                if (stack == 0) cnt++;
            }
        }
        return cnt;
    }

    private String inner(String s) {
        return s.substring(1, s.length() - 1);
    }

    private void fill(int n) {
        for (int i = 0; i < n + 1; i++) {
            if (i == 0) {
                cache[i] = "{}";
            } else if (i == 1) {
                cache[i] = "{{}}";
            } else {
                cache[i] = "{" + inner(cache[i - 1]) + "," + cache[i - 1] + "}";
            }
        }
    }

    private void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int iterations = Integer.parseInt(br.readLine());

        for (int i = 0; i < iterations; i++) {
            String first = br.readLine();
            String second = br.readLine();

            int answer = parse(first) + parse(second);
            fill(answer);

            System.out.println(cache[answer]);
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }
}
