#import "Basic";
#import "Math";

tschebyschef_distance :: (x : [] float, y : [] float) -> float {

    assert(x.count == y.count, "Die Daten Vektoren haben nicht die selbe Laenge!");

    z : [..] float;
    for x {
        array_add(*z, x[it_index] - y[it_index]);
    }
    print("Worked");
    max := 0.0;
    for it_index: 0..x.count {
        if abs(z[it_index]) > max {
            max = abs(z[it_index]);
        }
    }

    return max;
    
}

manhattan_distance :: (x : [] float, y : [] float) -> float {

    assert(x.count == y.count, "Die Daten Vektoren haben nicht die selbe Laenge!");

    distance := 0.0;
    for x {
        distance += abs(x[it_index] - y[it_index]);
    }

    return distance;
}

main :: () {
    x : [2] float;
    y : [2] float;

    x[0] = 3; 
    x[1] = 2;

    y[0] = 1;
    y[1] = 0;

    print("%\n", tschebyschef_distance(x, y));
    print("%\n", manhattan_distance(x, y));
}