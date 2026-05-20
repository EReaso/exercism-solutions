import kotlin.math.pow
import kotlin.math.sqrt


object Darts {
    private fun distance(x: Double, y: Double): Double {
        return sqrt(x.pow(2.0) + y.pow(2.0))
    }
    
    fun score(x: Number, y: Number): Int {
        val dist = distance(x.toDouble(), y.toDouble())
        return when {
            dist > 10.0 -> 0
            dist > 5.0 -> 1
            dist > 1.0 -> 5
            else -> 10
        }
    }
}
