import org.scalatest.FunSuite

class FibnTest extends FunSuite {
  test("Fibn.fib") {
    assert(Fibn.fib(3) === 2)
  }
}

