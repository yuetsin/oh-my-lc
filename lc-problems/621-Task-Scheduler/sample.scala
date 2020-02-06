  object Solution {
    import scala.collection.mutable

    def leastInterval(tasks: Array[Char], n: Int): Int = {
      val priorityQueue: mutable.PriorityQueue[(Char, Int)] = mutable.PriorityQueue[(Char, Int)](tasks
        .groupBy(identity)
        .mapValues(_.length)
        .toSeq: _*
      )(Ordering.by(task => task._2))

      def loop(now: Int, coolDown: Map[Int, (Char, Int)]): Int = {
        if (coolDown.contains(now)) {
          priorityQueue.enqueue(coolDown(now))
          loop(now, coolDown - now)
        }
        else if (priorityQueue.nonEmpty) {
          val task: (Char, Int) = priorityQueue.dequeue()

          if (task._2 > 1) loop(now + 1, coolDown + (now + n + 1 -> (task._1, task._2 - 1)))
          else loop(now + 1, coolDown)
        }
        else if (priorityQueue.isEmpty && coolDown.isEmpty) now
        else loop(now + 1, coolDown)
      }

      loop(0, Map.empty)
    }
  }