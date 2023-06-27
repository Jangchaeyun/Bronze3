import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int player, nowTime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        player = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int question = Integer.valueOf(st.nextToken());

        for (int i = 0; i < question; i++) {
            st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            String answer = st.nextToken();
            if (nowTime + time > 210) {
                break;
            }
            if (answer.equals("T")) {
                if (++player > 8) {
                    player = 1;
                }
            }
            nowTime += time;
        }
        System.out.println(player);
    }
}
