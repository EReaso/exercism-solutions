class School {
    var enrolled = mutableMapOf<Int, MutableSet<String>>()
    
    fun add(student: String, grade: Int) {
        val gradeSet = enrolled.getOrPut(grade) {mutableSetOf<String>()}
        gradeSet.add(student)
    }

    fun grade(grade: Int): List<String> {
        return enrolled[grade]?.sorted() ?: emptyList()
    }

    fun roster(): List<String> {
        return enrolled.toSortedMap().flatMap {
            it.value.sorted()
        }
    }
}
