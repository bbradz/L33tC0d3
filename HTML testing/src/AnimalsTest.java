public class AnimalsTest {

    Dillo babyDillo = new Dillo(5,false);
    /**
     * Example test method.
     * Test methods must have @Test before the method
     */
    @Test
    public void testExample() {
        // example syntax for assertEquals
        Assert.assertEquals(1+1, 2);
    }
    @Test
    public void testMakeDillo() {
        Assert.assertEquals(babyDillo.length, 5);
    }
}
