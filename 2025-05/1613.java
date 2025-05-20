import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static boolean[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numNodes = Integer.parseInt(st.nextToken());
        int numEdges = Integer.parseInt(st.nextToken());

        graph = new boolean[numNodes + 1][numNodes + 1];
        for (int i = 0; i < numNodes + 1; i++) {
            for (int j = 0; j < numNodes + 1; j++) {
                graph[i][j] = i == j;
            }
        }

        while (numEdges-- > 0) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            graph[src][dst] = true;
        }

        floydWarshall();

        int numCases = Integer.parseInt(br.readLine());
        while (numCases-- > 0) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            if (graph[src][dst]) {
                System.out.println(-1);
            } else if (graph[dst][src]) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }

    static void floydWarshall() {
        for (int k = 1; k < graph.length; k++) {
            for (int i = 1; i < graph.length; i++) {
                for (int j = 1; j < graph.length; j++) {
                    if (graph[i][k] && graph[k][j]) {
                        graph[i][j] = true;
                    }
                }
            }
        }
    }
}
