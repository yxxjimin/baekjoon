import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    private static final Map<Integer, Integer> DIGIT_SUM_CACHE = Map.of(
            0, 0, 1, 1, 2, 3, 3, 6, 4, 10, 5, 15,
            6, 21, 7, 28, 8, 36, 9, 45
    );

    private static long getSumBelow(long num) {
        if (num < 0) return 0;

        long sum = 0;
        int length = String.valueOf(num).length();

        for (int i = 0; i < length; i++) {
            long div = (long) Math.pow(10, i);
            long prefix = num / (div * 10);
            long curr = (num / div) % 10;
            long suffix = num % div;

            long prefixSum = DIGIT_SUM_CACHE.get(9) * (prefix * div);
            long currSum = DIGIT_SUM_CACHE.getOrDefault((int) curr - 1, 0) * div;
            long suffixSum = curr * (suffix + 1);

            sum += prefixSum + currSum + suffixSum;
        }

        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int numCases = Integer.parseInt(bf.readLine());
        while (numCases-- > 0) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            long lower = Long.parseLong(st.nextToken());
            long upper = Long.parseLong(st.nextToken());
            System.out.println(getSumBelow(upper) - getSumBelow(lower - 1));
        }
    }
}
