object Fibn {

  def fib(input: Int): Int = {
    var prev = 1
    var next = 1
    var n = 1

    while (n < input) {
      n += 1
      val temp = prev + next
      prev = next
      next = temp
    }

    next
  }
}
