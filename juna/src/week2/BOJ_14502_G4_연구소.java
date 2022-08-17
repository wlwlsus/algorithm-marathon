package week2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_14502_G4_연구소 {
	
	static int N, M;
	static int ans = 0;
	static int[][] board, tboard;
	static int[] dy = {1, -1, 0, 0};
	static int[] dx = {0, 0, 1, -1};
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		// 1. 입력
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				board[i][j] = Integer.parseInt(st.nextToken());
		}
		
		// 2. 풀이
		wall(0, 0, 0);
		
		// 3. 출력
		System.out.println(ans);

	}
	
	
	// wall : 벽을 세우는 메서드 (조합 공식 응용)
	// sy, sx : 시작 정점 좌표
	// cnt : 현재까지 세운 벽의 개수
	private static void wall(int sy, int sx, int cnt) {
		
		if (cnt == 3) {
			virus();
			return ;
		}
		
		for (int y = sy; y < N; y++)
			for (int x = 0; x < M; x++) {
				
				// 좌표 (sy, sx)에서부터 탐색을 시작할 수 있게끔 x값 보정하기
				if (y == sy && x < sx) {
					x = sx;
					continue;
				}
				
				if (board[y][x] == 0) {
					board[y][x] = 1;
					wall(y, x, cnt + 1);
					board[y][x] = 0;
				}
			}
		
	}
	
	
	// virus : 바이러스를 퍼뜨리는 메서드
	private static void virus() {
		
		// 1. 바이러스를 퍼뜨린 결과를 저장할 배열, tboard를 board를 copy하여 생성
		tboard = new int[N][M];
		for (int i = 0; i < N; i++)
			tboard[i] = Arrays.copyOf(board[i], M);
		
		// 2. bfs를 이용해서 바이러스 퍼뜨리기
		for (int y = 0; y < N; y++)
			for (int x = 0; x < M; x++)
				if (tboard[y][x] == 2)
					bfs(y, x);
			
		// 3. 0 개수 세기
		int tot = 0;
		for (int y = 0; y < N; y++)
			for (int x = 0; x < M; x++)
				if (tboard[y][x] == 0)
					tot++;
		ans = Math.max(ans, tot);
		
	}
	
	
	// bfs : 그래프를 순회하며 바이러스를 퍼뜨린다.
	// sy, sx : 시작 정점 좌표
	private static void bfs(int sy, int sx) {
		
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[] {sy, sx});
		
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			int y = tmp[0];
			int x = tmp[1];
			
			for (int k = 0; k < 4; k++) {
				int ny = y + dy[k];
				int nx = x + dx[k];
				
				if (0 <= ny && ny < N && 0 <= nx && nx < M && tboard[ny][nx] == 0) {
					tboard[ny][nx] = 2;
					q.offer(new int[] {ny, nx});
				}
			}
		}
	}
}
