
"""
解法一
简单粗暴，先将两个数组合并，两个有序数组的合并也是归并排序中的一部分。然后根据奇数，还是偶数，返回中位数。

解法二
双指针

解法三
求中位数，其实就是求第 k 小数的一种特殊情况，而求第 k 小数有一种算法。
假设我们要找第 k 小数，我们可以每次循环排除掉 k/2 个数。看下边一个例子。

更一般的情况 A[1] ，A[2] ，A[3]，A[k/2] ... ，B[1]，B[2]，B[3]，B[k/2] ... ，如果 A[k/2]<B[k/2] ，那么A[1]，A[2]，A[3]，A[k/2]都不可能是第 k 小的数字。

A 数组中比 A[k/2] 小的数有 k/2-1 个，B 数组中，B[k/2] 比 A[k/2] 小，假设 B[k/2] 前边的数字都比 A[k/2] 小，也只有 k/2-1 个，所以比 A[k/2] 小的数字最多有 k/1-1+k/2-1=k-2个，所以 A[k/2] 最多是第 k-1 小的数。而比 A[k/2] 小的数更不可能是第 k 小的数了，所以可以把它们排除。

我们每次都是取 k/2 的数进行比较，有时候可能会遇到数组长度小于 k/2的时候。
此时 k / 2 等于 3，而上边的数组长度是 2，我们此时将箭头指向它的末尾就可以了。这样的话，由于 2 < 3，所以就会导致上边的数组 1，2 都被排除。造成下边的情况。


"""
