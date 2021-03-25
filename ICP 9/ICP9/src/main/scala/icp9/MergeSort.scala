package icp9

import org.apache.spark._

object MergeSort {
  def main(args: Array[String]) {

    System.setProperty("hadoop.home.dir","C:\\spark-3.1.1-bin-hadoop3.2")
    val conf = new SparkConf().setAppName("merge sort").setMaster("local[*]")
    // Create a Scala Spark Context.
    val sc = new SparkContext(conf)
    def mergeSort(xs: List[Int]): List[Int] = {
      val n = xs.length / 2
      if (n == 0) xs
      else
      {
        val (left, right) = xs splitAt(n)
        merge(mergeSort(left), mergeSort(right))
      }
    }

    println(mergeSort(List(7,1,90,3,5,8)))
  }

  def merge(xs: List[Int], ys: List[Int]): List[Int] =
    (xs, ys) match {
      case(Nil, ys) => ys
      case(xs, Nil) => xs
      case(x :: xs1, y :: ys1) =>
        if (x < y) x::merge(xs1, ys)
        else y :: merge(xs, ys1)
    }
}
