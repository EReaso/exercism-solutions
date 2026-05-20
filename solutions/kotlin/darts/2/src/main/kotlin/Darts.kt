import kotlin.math.hypot


object Darts {
    fun score(x: Number, y: Number): Int {
        val dist = hypot(x.toDouble(), y.toDouble())
        return when {
            dist > 10.0 -> 0
            dist > 5.0 -> 1
            dist > 1.0 -> 5
            else -> 10
        }
    }
}
