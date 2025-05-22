import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static final int MAX_EDGE_DISTANCE = 50 * 20;
    private static final String SUCCESS = "happy";
    private static final String FAILED = "sad";

    static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int distanceTo(Node other) {
            return Math.abs(this.x - other.x) + Math.abs(this.y - other.y);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numCases = Integer.parseInt(br.readLine());

        while (numCases-- > 0) {
            int numStores = Integer.parseInt(br.readLine());
            List<Node> locations = new ArrayList<>();

            StringTokenizer st = new StringTokenizer(br.readLine());
            locations.add(
                    new Node(
                            Integer.parseInt(st.nextToken()),
                            Integer.parseInt(st.nextToken())
                    )
            );

            for (int i = 0; i < numStores; i++) {
                st = new StringTokenizer(br.readLine());
                locations.add(
                        new Node(
                                Integer.parseInt(st.nextToken()),
                                Integer.parseInt(st.nextToken())
                        )
                );
            }

            st = new StringTokenizer(br.readLine());
            locations.add(
                    new Node(
                            Integer.parseInt(st.nextToken()),
                            Integer.parseInt(st.nextToken())
                    )
            );

            System.out.println(solve(locations));
        }
    }

    private static String solve(List<Node> locations) {
        boolean[] visited = new boolean[locations.size()];

        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        visited[0] = true;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            Node node = locations.get(curr);
            for (int next = 0; next < locations.size(); next++) {
                if (!visited[next] && locations.get(next).distanceTo(node) <= MAX_EDGE_DISTANCE) {
                    if (next == locations.size() - 1) return SUCCESS;
                    queue.add(next);
                    visited[next]= true;
                }
            }
        }

        return FAILED;
    }
}
