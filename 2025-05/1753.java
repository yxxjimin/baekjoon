import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static Map<Integer, List<int[]>> graph;
    static int[] distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numNodes = Integer.parseInt(st.nextToken());
        int numEdges = Integer.parseInt(st.nextToken());
        int root = Integer.parseInt(br.readLine());

        graph = new HashMap<>();
        distance = new int[numNodes + 1];

        for (int i = 1; i < numNodes + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
            graph.put(i, new ArrayList<>());
        }

        while (numEdges-- > 0) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            int wgt = Integer.parseInt(st.nextToken());

            graph.get(src).add(new int[]{dst, wgt});
        }

        dijkstra(root);

        for (int i = 1; i < numNodes + 1; i++) {
            System.out.println(distance[i] == Integer.MAX_VALUE ? "INF" : distance[i]);
        }
    }

    static void dijkstra(int root) {
        PriorityQueue<int[]> queue = new PriorityQueue<>((u, v) -> u[1] - v[1]);

        distance[root] = 0;
        queue.add(new int[]{root, distance[root]});

        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int src = node[0];

            if (distance[src] < node[1]) continue;

            for (int[] adj : graph.get(src)) {
                int dst = adj[0], wgt = adj[1];
                int relaxed = distance[src] + wgt;
                if (relaxed < distance[dst]) {
                    distance[dst] = relaxed;
                    queue.add(new int[]{dst, distance[dst]});
                }
            }
        }
    }
}
