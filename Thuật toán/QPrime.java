import java.util.Scanner;

public class QPrime {

    public static int count(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0)
             count++;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap so nguyen duong N: ");
        int N = scanner.nextInt();

        System.out.println("Cac so Q-prime nho hon or bang " + N + " là:");
        for (int i = 1; i <= N; i++) {
            if (count(i) == 4) {
                System.out.print(i + " ");
            }
        }
        scanner.close();
    }
}
