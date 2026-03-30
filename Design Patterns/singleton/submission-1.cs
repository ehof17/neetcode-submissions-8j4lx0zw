public class Singleton {
    private string value = null;
    private static Singleton unique = null;
    private Singleton() {
    
    }

    public static Singleton getInstance() {
        if (unique == null){
            unique = new Singleton();
        }
        return unique;
    }

    public string getValue() {
        return this.value;
    }

    public void setValue(string value){
        this.value = value;
    }
}
