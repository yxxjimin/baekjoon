import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    static int[][] weights;
    static boolean[] visited;
    static int connected = 0;

    static int charToWeight(char ch) {
        if (ch == '0') return Integer.MAX_VALUE;
        if (ch >= 'a') return ch - 'a' + 1;
        return ch - 'A' + 27;
    }

    static int prim() {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);
        int result = 0;

        pq.offer(new int[]{0, 0});

        while (!pq.isEmpty() && connected < visited.length) {
            int[] tgt = pq.poll();
            int dist = tgt[0], node = tgt[1];
            if (visited[node]) continue;

            result += dist;
            connected++;
            visited[node] = true;

            for (int i = 0; i < weights[node].length; i++) {
                int wgt = Math.min(weights[node][i], weights[i][node]);
                if (!visited[i] && wgt < Integer.MAX_VALUE) {
                    pq.offer(new int[]{wgt, i});
                }
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numNodes = Integer.parseInt(br.readLine());

        weights = new int[numNodes][numNodes];
        visited = new boolean[numNodes];

        int totalWeights = 0;

        for (int i = 0; i < numNodes; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                int wgt = charToWeight(line.charAt(j));
                totalWeights += wgt < Integer.MAX_VALUE ? wgt : 0;
                weights[i][j] = wgt;
            }
        }

        int result = totalWeights - prim();
        System.out.println(connected == numNodes ? result : -1);
    }
}
