"""
用返回0~6随机数的函数构造返回0~9随机数的函数
想到这个就是我们的关键，接下来就是想办法构造函数使得产生的每个数都是唯一的。我们不难想到把第一个rand6()产生的随机数a放在个位上，而把第二个rand6()产生的随机数b放在十位上，所有可能为：00~06,10~16,20~26,30~36，40~46,50~56，60~66。很容易看出这些就是7进制数，所以我们用rand6()*7+rand6()就能生成0~49范围的随机数，而且每个数产生的概率相等，都是1/49。产生40~49之间的随机数时不保留而重新产生一个新的随机数，这样产生0~39之间的数也是等概率的，仍然都是1/49，对于产生的数我们记为r（0<= r <=39），则 r/4 即可返回0~9范围的数。而且 r 取0~3这四个数时 r/4 返回0，r 取4~7这四个数时 r/4 返回1，……，r 取36~39这四个数时 r/4 返回9。因此返回0~9范围的每个数字的概率都是4/49，满足等概率。
对于产生的数我们记为r（0<= r <=39），则 r/4 即可返回0~9范围的数。

int rand9()               // 用rand6()编写随机产生0~9之间的数
{
    int a, b, r;
    do{
        a = rand6();    // 随机产生0~6之间的数
        b = rand6();
        r = a * 7 + b;
    } while (r >= 40);

    return r / 4;
}
"""

"""
给定一个 0-4随机数生成器 如何生成0-6随机数并验证？
n进制计算
我们把0-6进行排列，这样可以得到44=16个数字，而且每一个数字都是唯一的，最后一个44其实就是5进制的2位数。换算成10进制就是45 + 4 = 24, 就是0-24 共计25个数字。
需要0-6共7个数字，7*3=21
public static int rand6() {
        int result = rand4() * 5 + rand4();
        do {
            result = rand4() * 5 + rand4();
        } while (result > 20);
        return result / 3;
    }
"""
