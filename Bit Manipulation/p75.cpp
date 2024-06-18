/*

Problem: 371. Sum of Two Integers

URL: https://leetcode.com/problems/sum-of-two-integers/description/

Author: Harshit Allumolu <hallumol@asu.edu>

*/

int getSum(int a, int b) {
    if(b == 0)
        return a;
    return getSum((a ^ b), (a & b) << 1);
}