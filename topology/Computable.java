public interface Computable {
    int compute( int x, int y );
}

// =======================================================

public class Addition implements Computable {
    int compute( int x, int y) {
        return x + y;
    }
}

// =======================================================

public class Subtraction implements Computable {
    int compute( int x, int y) {
        return x - y;
    }
}

// =======================================================

public class Multiplication implements Computable {
    int compute( int x, int y) {
        return x * y;
    }
}

// =======================================================

public class ArrayComputation {
    private Integer[] values;
    public Structure( Integer[] p ) { values = p; }


    public int compute_for_array( Computable compute ) {
        int result = 0;
        for ( int i = 0; i < values.length; i++ ) {
            result = compute(values[i], result);
        }

        return result;
    }
}

// =======================================================

class Main {
    public static void main(String[] args) {
        Integer[] intArray = new Integer[]{ 0, 1, 2, 3, 4 };
        ArrayComputation AC = new ArrayComputation(intArray);


        result = AC.compute_for_array(Addition);

        System.out.println(result); // 10

        result = AC.compute_for_array(Subtraction);

        System.out.println(result); // -10

        result = AC.compute_for_array(( x, y) -> { return x * y; }

        )
    }
}