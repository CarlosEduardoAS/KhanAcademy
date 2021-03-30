var insert = function(array, rightIndex, value) {
    for(var j = rightIndex;
        j >= 0 && array[j] > value;
        j--) {
        array[j + 1] = array[j];
    }   
    array[j + 1] = value; 
};

var insertionSort = function(array) {
    for (var st = 1; st < array.length; st++) {
        insert(array, st - 1, array[st]);
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

var array = [0, -4, 100, -32, 3, 5];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [-32, -4, 0, 3, 5, 100]);
