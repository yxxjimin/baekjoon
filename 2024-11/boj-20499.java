import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> scores = Arrays
                                .asList(br.readLine().split("/"))
                                .stream()
                                .map(s -> Integer.parseInt(s))
                                .collect(Collectors.toList());

        int k = scores.get(0);
        int d = scores.get(1);
        int a = scores.get(2);

        if (k + a < d || d == 0) {
            System.out.println("hasu");
        } else {
            System.out.println("gosu");
        }
    }
}
