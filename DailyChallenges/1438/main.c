#include<stdio.h>

int longestSubarray(int* nums, int numsSize, int limit) {
    int* a=&nums[0];
    printf("%d",*a);


}
int main(){

    return 0;
    int nums[4]={8,2,4,7};
    int numsize=sizeof(nums)/sizeof(nums[0]);

    int limit=4;
    longestSubarray(nums,numsize,limit);
}
