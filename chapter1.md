### Arguments pass by value
java argument传的是值，例如一下代码块不会改变原有赋值
    
    int i = 2;
    changeValueToOne(i);
    System.out.println(i); // i 仍然是2

当传的是array的时候，因为传进方法的是alias, 可以理解为是指针类似的概念，改变b的index的值也会同时改变a的值

    int[] a = { 1, 2, 3 };
    int[] b = a;
    b[0] = 2;
    System.out.println(a[0]); // 2

    int[] a = { 3, 2, 1 };
    Arrays.sort(a);
    System.out.println(Arrays.toString(a)); // { 1, 2, 3 } sorted

