
import org.junit.Assert;
import org.junit.Test;

public class TriangleTestCases {
    @Test
    public void testBadInput() {
        /* 每一位都独立犯错，确保都能触发 invalidInput */

        /* 向下越界 */
        Assert.assertEquals(Triangle.startRun(0, 0, 0), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(0, 0, 1), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(0, 1, 0), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(0, 1, 1), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(1, 0, 0), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(1, 0, 1), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(1, 1, 0), Strings.invalidInput);

        /* 向上越界 */
        Assert.assertEquals(Triangle.startRun(201, 201, 201), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(201, 201, 1), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(201, 1, 201), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(201, 1, 1), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(1, 201, 201), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(1, 201, 1), Strings.invalidInput);
        Assert.assertEquals(Triangle.startRun(1, 1, 201), Strings.invalidInput);

        /* 一些正常边长度的输入 */
        Assert.assertNotEquals(Triangle.startRun(3, 1, 199), Strings.invalidInput);
        Assert.assertNotEquals(Triangle.startRun(6, 4, 30), Strings.invalidInput);
        Assert.assertNotEquals(Triangle.startRun(3, 1, 15), Strings.invalidInput);
    }

    @Test
    public void testCantFormTriangle() {
        /* 不可以构成三角形的边组合 */
        Assert.assertEquals(Triangle.startRun(1, 1, 2), Strings.cantFormTriangle);
        Assert.assertEquals(Triangle.startRun(2, 2, 5), Strings.cantFormTriangle);
        Assert.assertEquals(Triangle.startRun(4, 7, 13), Strings.cantFormTriangle);
        Assert.assertEquals(Triangle.startRun(4, 8, 12), Strings.cantFormTriangle);

        /* 可以构成三角形的边组合 */
        Assert.assertNotEquals(Triangle.startRun(4, 7, 10), Strings.cantFormTriangle);
        Assert.assertNotEquals(Triangle.startRun(4, 8, 9), Strings.cantFormTriangle);
    }

    @Test
    public void testEvenTriangle() {
        /* 正常的等边三角形 */
        Assert.assertEquals(Triangle.startRun(1, 1, 1), Strings.allEqualTriangle);
        Assert.assertEquals(Triangle.startRun(2, 2, 2), Strings.allEqualTriangle);
        Assert.assertEquals(Triangle.startRun(5, 5, 5), Strings.allEqualTriangle);

        /* 不能构成三角形 */
        Assert.assertNotEquals(Triangle.startRun(0, 0, 0), Strings.allEqualTriangle);
        Assert.assertNotEquals(Triangle.startRun(-5, -5, 0), Strings.allEqualTriangle);
    }

    @Test
    public void testTwoEqualTriangle() {
        /* 正常的普通等腰三角形 */
        Assert.assertEquals(Triangle.startRun(1, 2, 2), Strings.twoEqualTriangle);
        Assert.assertEquals(Triangle.startRun(4, 5, 4), Strings.twoEqualTriangle);
        Assert.assertEquals(Triangle.startRun(2, 2, 3), Strings.twoEqualTriangle);

        /* 会进化为等边三角形 */
        Assert.assertNotEquals(Triangle.startRun(3, 3, 3), Strings.twoEqualTriangle);

        /* 不能构成三角形 */
        Assert.assertNotEquals(Triangle.startRun(5, 2, 2), Strings.twoEqualTriangle);
    }

    @Test
    public void testPeculiarTriangle() {
        /* 正常的普通直角三角形 */
        Assert.assertEquals(Triangle.startRun(3, 4, 5), Strings.peculiarTriangle);
        Assert.assertEquals(Triangle.startRun(6, 8, 10), Strings.peculiarTriangle);

        /* 错误的输入 */
        Assert.assertNotEquals(Triangle.startRun(-3, 4, 5), Strings.peculiarTriangle);
        Assert.assertNotEquals(Triangle.startRun(4, 4, 0), Strings.peculiarTriangle);
    }

    @Test
    public void testTrivialTriangle() {
        /* 正常的普通三角形 */
        Assert.assertEquals(Triangle.startRun(3, 4, 6), Strings.normalTriangle);
        Assert.assertEquals(Triangle.startRun(6, 7, 10), Strings.normalTriangle);

        /* 一些特别的三角形 */
        Assert.assertNotEquals(Triangle.startRun(3, 4, 5), Strings.normalTriangle);
        Assert.assertNotEquals(Triangle.startRun(4, 4, 4), Strings.normalTriangle);
        Assert.assertNotEquals(Triangle.startRun(6, 8, 8), Strings.normalTriangle);
        Assert.assertNotEquals(Triangle.startRun(0, 1, 1), Strings.normalTriangle);
    }
}
