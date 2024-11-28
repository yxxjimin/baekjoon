import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String series = br.readLine();

        long answer = 0L;
        long denominator = 1000000007L;
        long currFlips = 1L;

        for (int i = 0; i < series.length(); i++) {
            if (series.charAt(i) == 'O') {
                answer += currFlips;
                answer %= denominator;
            }
            currFlips *= 2;
            currFlips %= denominator;
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }
}
