import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

/**
 * Title: 백준 20207번
 * Comment: 날짜별로 일정 개수 카운트해서 일정 개수 0인 날 직전까지의 직사각형 크기 계산
 */
public class Main {

    static int[] schedulesCount = new int[366];

    private static int getTotalSize() {
        int totalSize = 0;
        int windowLength = 0;
        int windowDepth = 0;
        for (int i = 1; i < 366; i++) {
            if (schedulesCount[i] == 0) {
                totalSize += windowLength * windowDepth;
                windowLength = 0;
                windowDepth = 0;
            } else {
                windowLength++;
                windowDepth = Math.max(windowDepth, schedulesCount[i]);
            }
        }

        // 마지막 날 일정이 있는 경우
        totalSize += windowLength * windowDepth;
        return totalSize;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numCases = Integer.parseInt(br.readLine());
        while (numCases-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            IntStream.rangeClosed(start, end).forEach(i -> schedulesCount[i]++);
        }

        int totalSize = getTotalSize();

        System.out.println(totalSize);
    }
}

