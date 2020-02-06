class MyCircularQueue(_k: Int) {
  /** Initialize your data structure here. Set the size of the queue to be k. */
  var size: Int = _k
  var head: Int = 0
  var tail: Int = -1
  var count: Int = 0

  var queue: Array[Int] = new Array[Int](size)

  /** Insert an element into the circular queue. Return true if the operation is successful. */
  def enQueue(value: Int): Boolean = {
    if (isFull())
      false
    else {
      tail = (tail + 1) % size
      count +=1

      queue(tail) = value

      true
    }
  }

  /** Delete an element from the circular queue. Return true if the operation is successful. */
  def deQueue(): Boolean = {
    if (isEmpty())
      false
    else {
      head += 1 % size
      count -= 1

      true
    }
  }

  /** Get the front item from the queue. */
  def Front(): Int = {
    if (isEmpty())
      -1
    else queue(head)
  }

  /** Get the last item from the queue. */
  def Rear(): Int = {
    if (isEmpty())
      -1
    else queue(tail)
  }

  /** Checks whether the circular queue is empty or not. */
  def isEmpty(): Boolean = {
    count == 0
  }

  /** Checks whether the circular queue is full or not. */
  def isFull(): Boolean = {
    count == size
  }
}