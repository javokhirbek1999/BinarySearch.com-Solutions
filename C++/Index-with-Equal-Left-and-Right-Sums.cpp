int solve(vector<int>& nums) {
    int sum = 0;

    for (int i = 0; i<nums.size(); i++) {
        sum+=nums[i];
    }

    sum -= nums[0];

    if (sum == 0) {
        return 0;
    }

    int prefix, suffix;
    
    prefix = 0;
    suffix = sum+nums[0];

    for (int i = 0; i<nums.size(); i++) {
        suffix-=nums[i];
        if (prefix == suffix) {
            return i;
        }
        prefix+=nums[i];
    }

    return -1;

}
