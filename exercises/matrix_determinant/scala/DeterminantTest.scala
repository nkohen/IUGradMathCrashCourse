import org.scalatest.FunSuite

class DeterminantTest extends FunSuite {

  test("Test on two matrices") {

    val A1 =
      SquareMatrix(dim = 3,
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
      )

    assert(A1.determinant === 0)
    assertThrows[IllegalArgumentException](SquareMatrix(A1.cols.tail))

    val A2 = SquareMatrix(dim = 5,
      1, 2, 2, 5, -6,
      -1 ,1 ,5 ,7 ,-7,
      3, 5, 4, 4, 4,
      5, 4, 7, 2, 5,
      4, 1, 8, 1, 5
    )

    assert(A2.determinant === 904)
  }
}

