import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Title: 백준 1309번
 * Comment: N+1의 모든 경우 = 2 * (N에 사자를 넣는 경우) + (N에 사자를 안넣는 경우 = N-1의 모든 경우)
 */
public class Main {

    private void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int rowCnt = Integer.parseInt(br.readLine());
        final int divisor = 9901;

        int curr = 1;
        int prev = 1;
        int next;

        // Bottom-Up
        for (int i = 0; i < rowCnt; i++) {
            next = (2 * curr + prev) % divisor;
            prev = curr;
            curr = next;
        }

        System.out.println(curr);
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }
}
