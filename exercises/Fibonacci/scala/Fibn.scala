object Fibn {
  def fib(x: Int) = {
    var f1 = 1
    var f2 = 1
    var n = 1
    var temp = 1
    if (x<3) 1
    else {
      while (n+1<x) {
        n += 1
        temp = f1 + f2
        f1 = f2
        f2 = temp
      }
      temp
    }
  }
}

