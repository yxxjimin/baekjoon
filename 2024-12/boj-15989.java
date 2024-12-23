import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Title: 백준 15989번
 * Comment: 처음엔 3만 사용하는 케이스 -> 2, 3을 사용하는 케이스 -> 1, 2, 3을 사용하는 케이스로 접근했었는데 이러면 배열
 *      세 개를 각각 따로 선언해야 됨 (메모리 사용량 41212KB). 근데 반대로 1만 사용하는 케이스 -> 1, 2를 사용하는 케이스
 *      -> 1, 2, 3을 사용하는 케이스로 접근하면 in-place로 하나의 배열로 해결할 수 있음 (메모리 사용량 24644KB).
 */
public class Main {

    static int solve2(int n) {
        if (n < 3) return n;
        int[] a = new int[n + 1];

        // 1만 사용
        Arrays.fill(a, 1);

        // 1, 2 사용
        for (int i = 2; i < n + 1; i++) {
            a[i] += a[i - 2];
        }

        // 1, 2, 3 사용
        for (int i = 3; i < n + 1; i++) {
            a[i] += a[i - 3];
        }

        return a[n];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num_cases = Integer.parseInt(br.readLine());
        while (num_cases-- > 0) {
            int number = Integer.parseInt(br.readLine());
            System.out.println(solve2(number));
        }
    }
}

