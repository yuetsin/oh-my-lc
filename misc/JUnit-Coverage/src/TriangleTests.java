import junit.framework.TestCase;

public class TriangleTests extends TestCase {

    static TriangleTestCases tTC;
    @Override
    protected void setUp() throws Exception {
        super.setUp();
        System.out.println("Triangle Test Case triggered");
        tTC = new TriangleTestCases();
    }

    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    public void testCases() {
        tTC.testBadInput();
        System.out.println("Passed Bad Input Test (1 / 6)");
        tTC.testCantFormTriangle();
        System.out.println("Passed Bad Formation Test (2 / 6)");
        tTC.testEvenTriangle();
        System.out.println("Passed Equilateral Triangle Test (3 / 6)");
        tTC.testPeculiarTriangle();
        System.out.println("Passed Right Triangle Test (4 / 6)");
        tTC.testTwoEqualTriangle();
        System.out.println("Passed Isosceles Input Test (5 / 6)");
        tTC.testTrivialTriangle();
        System.out.println("Passed Trivial Input Test (6 / 6)");
    }
}
