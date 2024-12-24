import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Title: 백준 12915번
 * Comment: E / EM + M + MH / H 로 시작해서 E가 최소일 경우 EM에서 하나 나눠주고, H가 최소일 경우 MH에서 하나 나눠주는
 *      방식으로 풀었음. 처음엔 조건식을 easy == Math.min(...) 으로 달아놨는데 이러면 모든 난이도의 문제 개수가 동일할
 *      때에도 문제를 나눠주는 경우가 발생함 (e.g. 2 3 3 2 2). 그래서 조건식을 easy < hard && easy < midTotal 로
 *      변경해서 해결했음.
 */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int easy = Integer.parseInt(st.nextToken());
        int easyMid = Integer.parseInt(st.nextToken());
        int mid = Integer.parseInt(st.nextToken());
        int midHard = Integer.parseInt(st.nextToken());
        int hard = Integer.parseInt(st.nextToken());

        int midTotal = easyMid + mid + midHard;

        while (midTotal > 0 && (easyMid > 0 || midHard > 0)) {
            if (easy < hard && easy < midTotal && easyMid > 0) {
                easy++;
                midTotal--;
                easyMid--;
            } else if (hard <= easy && hard < midTotal && midHard > 0) {
                hard++;
                midTotal--;
                midHard--;
            } else {
                break;
            }
        }

        System.out.println(Math.min(Math.min(easy, midTotal), hard));
    }
}

