class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();

        int st = 0;
        int en = n-1;

        while(st<=en){

            int mid = st + (en-st)/2;

            if((mid==0 || nums[mid-1] != nums[mid]) && (mid==n-1 || nums[mid+1] != nums[mid])) return nums[mid];


            int idx2;

            if(mid !=0 && nums[mid-1] == nums[mid]) idx2 = mid-1;
            else idx2 = mid + 1;



            int miniIdx = min(idx2,mid);
            

            if(miniIdx%2 == 0) st = mid+1;
            else en = mid-1;
        }


        return -1;


    }
};