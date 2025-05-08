import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numCards = Integer.parseInt(br.readLine());

        int[] sequence = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] numToIdx = new int[numCards];
        for (int i = 0; i < numCards; i++) {
            numToIdx[sequence[i] - 1] = i;
        }

        int answer = 1;
        boolean[] visited = new boolean[numCards];

        for (int i = 0; i < numCards; i++) {
            if (!visited[i]) {
                int cnt = 0;
                int curr = i;
                while (!visited[curr]) {
                    cnt++;
                    visited[curr] = true;
                    curr = numToIdx[curr];
                }
                answer = getCommonMultiple(answer, cnt);
            }
        }

        System.out.println(answer);
    }

    static int getCommonDivisor(int p, int q) {
        if (q == 0) return p;
        return getCommonDivisor(q, p % q);
    }

    static int getCommonMultiple(int p, int q) {
        int gcd = getCommonDivisor(p, q);
        return (p / gcd) * q;
    }
}
