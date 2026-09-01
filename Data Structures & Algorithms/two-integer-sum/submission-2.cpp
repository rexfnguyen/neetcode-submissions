class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for(int i=0; i<nums.size(); i++) {
            int gap = target - nums[i];

            if(seen.count(gap)) {
                return {seen[gap], i};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};
