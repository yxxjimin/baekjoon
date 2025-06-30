import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[][] dist;
    static final int INFINITY = Integer.MAX_VALUE;
    static int minCycle = INFINITY;

    static void floydWarshall() {
        for (int k = 0; k < dist.length; k++) {
            for (int i = 0; i < dist.length; i++) {
                for (int j = 0; j < dist.length; j++) {
                    if (dist[i][k] < INFINITY && dist[k][j] < INFINITY) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                    if (i == j) {
                        minCycle = Math.min(minCycle, dist[i][j]);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numNodes = Integer.parseInt(st.nextToken());
        int numEdges = Integer.parseInt(st.nextToken());
        dist = new int[numNodes][numNodes];

        for (int i = 0; i < numNodes; i++) {
            Arrays.fill(dist[i], INFINITY);
        }

        while (numEdges-- > 0) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken()) - 1;
            int dst = Integer.parseInt(st.nextToken()) - 1;
            int wgt = Integer.parseInt(st.nextToken());
            dist[src][dst] = wgt;
        }

        floydWarshall();

        System.out.println(minCycle < INFINITY ? minCycle : -1);
    }
}
