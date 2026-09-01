class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen_list;

        for(int i : nums) {
            if(seen_list.count(i)) {
                return true;
            }
            seen_list.insert(i);
        }
        return false;
    }
};