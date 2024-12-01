import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Title: 백준 1629번
 * Comment:
 *  (1) 변수 값 범위 꼭 확인하기
 *  (2) 부분 문제 쪼갤 때 O(log n) 확인
 */
public class Main {
    static long base;
    static long power;
    static long div;

    static long subProblem(long n) {
        if (n == 1) return base % div;

        long mid = n / 2;
        long midAnswer = subProblem(mid);
        if (n % 2 == 0) {
            return midAnswer * midAnswer % div;
        } else {
            return (midAnswer * midAnswer % div) * base % div;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        base = Long.parseLong(st.nextToken());
        power = Long.parseLong(st.nextToken());
        div = Long.parseLong(st.nextToken());

        long answer = subProblem(power);
        System.out.println(answer);
    }
}
