import java.util.HashMap;

class Solution1 {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> found = new HashMap<Integer, Integer>();
        for (int num: nums) {
            if (found.get(num) != null){
                if (found.get(num)==1){
                    return true;
                }
            }
            else {
                found.put(num, 1);
            }
        }
        return false;
    }
}