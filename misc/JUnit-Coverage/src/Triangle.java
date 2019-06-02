public class Triangle {
    //判断是否能构成三角形
    public static String JudgeTriangle(int a, int b, int c) {
        if (!(a + b > c && a + c > b && b + c > a)) {
            return Strings.cantFormTriangle;
        }
        return Strings.emptyString;
    }

    //判断是否能构成等腰三角形
    public static String JudgeDTriangle(int a, int b, int c) {
        if (a == b || a == c || b == c) {
            if (a == b && a == c) {
                return Strings.allEqualTriangle;
            } else {
                return Strings.twoEqualTriangle;
            }
        }
        return Strings.emptyString;
    }

    //判断是否是直角三角形
    public static String JudgeRTriangle(int a, int b, int c) {
        int r1, r2, r3;
        r1 = a * a + b * b - c * c;
        r2 = a * a + c * c - b;
        r3 = b * b + c * c - a * a;
        /*System.out.println(r1+r2+r3);*/
        if (r1 == 0 || r2 == 0 || r3 == 0) {
            return Strings.peculiarTriangle;
        }
        return Strings.emptyString;
    }

    static String startRun(int a, int b, int c) {

//判断输入三边是否合法
        if (a <= 0 || a > 200 || b <= 0 || b > 200 || c <= 0 || c > 200) {
            return Strings.invalidInput;
        } else {
//判断是否能构成三角形
            String judgeIsTriangle = JudgeTriangle(a, b, c);
            if (!judgeIsTriangle.equals(Strings.emptyString)) {
                return judgeIsTriangle;
            }
//判断是否是等腰或等边三角形
            String judgeDTriangle = JudgeDTriangle(a, b, c);
            if (!judgeDTriangle.equals(Strings.emptyString)) {
                return judgeDTriangle;
            }
//判断是否是直角三角形
            String judgeRTriangle = JudgeRTriangle(a, b, c);
            if (!judgeRTriangle.equals(Strings.emptyString)) {
                return judgeRTriangle;
            }
//判断是一般三角形
            return Strings.normalTriangle;
        }
    }
}