import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
    double distance;
    int node;

    public Node(double distance, int node) {
        this.distance = distance;
        this.node = node;
    }

    @Override
    public int compareTo(Node other) {
        return Double.compare(this.distance, other.distance);
    }
}

public class Main {
    static double[][] distance;
    static boolean[] visited;
    static PriorityQueue<Node> pq = new PriorityQueue<>();

    static double getDistance(int[] src, int[] dst) {
        int x1 = src[0], y1 = src[1];
        int x2 = dst[0], y2 = dst[1];
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    static double prim() {
        double distanceSum = 0;
        pq.offer(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (visited[node.node]) continue;
            visited[node.node] = true;
            distanceSum += node.distance;
            for (int i = 0; i < distance[node.node].length; i++) {
                pq.offer(new Node(distance[node.node][i], i));
            }
        }

        return distanceSum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numNodes = Integer.parseInt(st.nextToken());
        int numEdges = Integer.parseInt(st.nextToken());

        int[][] nodes = new int[numNodes][2];
        distance = new double[numNodes][numNodes];
        visited = new boolean[numNodes];

        for (int i = 0; i < numNodes; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodes[i] = new int[]{x, y};

            for (int j = 0; j < i; j++) {
                double dist = getDistance(nodes[i], nodes[j]);
                distance[i][j] = dist;
                distance[j][i] = dist;
            }
        }

        while (numEdges-- > 0) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken()) - 1;
            int dst = Integer.parseInt(st.nextToken()) - 1;
            distance[src][dst] = 0;
            distance[dst][src] = 0;
        }

        System.out.println(String.format("%.2f", prim()));
    }
}
