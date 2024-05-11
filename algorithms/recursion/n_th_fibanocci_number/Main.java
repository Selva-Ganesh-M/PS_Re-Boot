package recursion.n_th_fibanocci_number;

import java.util.Scanner;

/**
 * Main
 */
public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the position to find the fibanocci value: ");
        int pos = scan.nextInt();

        Test test = new Test();
        int ans_val = test.n_th_fibanocci(pos);

        String ans = String.format("the value of %dth position in the fibanocci series is %d", pos, ans_val);
        System.out.println(ans);
    }

}

class Test {
    public int n_th_fibanocci(int pos){
        if (pos == 0){
            return 0;
        }
        if (pos == 1){
            return 1;
        }
        return n_th_fibanocci(pos-2)+n_th_fibanocci(pos-1);
    }
}