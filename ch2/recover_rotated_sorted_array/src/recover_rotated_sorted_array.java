import java.util.ArrayList;

public class recover_rotated_sorted_array {
    private static void recoverHelper(ArrayList<Integer> nums, int start, int end){

        for(int i = start, j = end; i < j; i++, j--){
            int temp = nums.get(i);
            nums.set(i,nums.get(j));
            nums.set(j,temp);
        }
    }

    public static void recoverRotatedSortedArray(ArrayList<Integer> nums){
        if(nums == null || nums.size()==0){
            return;
        }

        for(int i = 0; i< nums.size()-1;i++){
            if(nums.get(i)> nums.get(i+1)){
                recoverHelper(nums, 0,i);
                recoverHelper(nums, i+1, nums.size()-1);
                recoverHelper(nums, 0, nums.size()-1);
                return;
            }
        }
    }

    public static void main(String[] args){
        ArrayList<Integer> a = new ArrayList<Integer>();
        a.add(4);
        a.add(5);
        a.add(1);
        a.add(2);
        a.add(3);
//        a.add(6);
        recoverRotatedSortedArray(a);
        System.out.println(a);
    }
}