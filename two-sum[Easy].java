import java.util.HashMap;

class Solution3 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> found = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++){
            Integer searching_for = target - nums[i];
            if (found.get(searching_for)!=null){
                int end[] = {i, found.get(searching_for)};
                return end;
            }
            else {
                found.put(nums[i], i);
            }
        }

        return null;
    }
}