
case class SquareMatrix(cols: Vector[Vector[Int]]) {

  val dim: Int = cols.length

  // error for non-square matrix input
  cols.foreach(col => require(col.length == dim))

  def determinant: Int = {
    var det = 0

    for (index <- cols.indices) {
      val colsWithoutCol = cols.take(index) ++ cols.takeRight(dim - index - 1)
      val minorCols = colsWithoutCol.map(_.tail)
      val minorDim = minorCols.length

      var detMinor = 0 // determinant of the minor
      if (minorDim != 1) {
        val B = SquareMatrix(minorCols)
        detMinor = B.determinant
      }
      else detMinor = minorCols(0)(0)

      det = det + (scala.math.pow(-1,index)*cols(index)(0)*detMinor).toInt
    }

    det
  }
}

object SquareMatrix {

  def apply(dim: Int, entries: Int*): SquareMatrix = {
    require(dim*dim == entries.length)

    var cols: Vector[Vector[Int]] = Vector.empty
    for (colIndex <- 0.until(dim)) {
      cols = cols.appended(
        entries
          .zipWithIndex
          .filter{ case (_, index) => index % dim == colIndex}
          .map { case (entry, _) => entry }
          .toVector
      )
    }

    SquareMatrix(cols)
  }
}

