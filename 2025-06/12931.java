import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        int[] numbers = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int cnt = 0;

        while (IntStream.of(numbers).sum() != 0) {
            boolean canHalve = true;
            for (int i = 0; i < numbers.length; i++) {
                if (numbers[i] % 2 != 0) {
                    numbers[i]--;
                    cnt++;
                    canHalve = false;
                }
            }

            if (canHalve) {
                cnt++;
                for (int i = 0; i < numbers.length; i++) {
                    numbers[i] /= 2;
                }
            }
        }

        System.out.println(cnt);
    }
}
