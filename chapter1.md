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

### 数据结构的例子
1. bag 就是一个包，不支持取出
2. queue 队列，排队，先进的先出
3. stack email后进入的在上面，好处是新的email会被先读到，坏处是老的不清空stack永远读不到 / 上网看网页，点了link就到了新网页上了(not _blank)，老网页必须点退回往回退

### 数据结构的应用
1. 算术运算的运用
    1. ( 无视
    2. 运算符 push进operator stack
    3. 数字 push进val stack
    4. ) pop 两个数字， 一个operator，进行运算后得到的结果push回val stack
    5. 最终合法的expression会留下一个val在val stack中，将其pop出来就得到了结果

