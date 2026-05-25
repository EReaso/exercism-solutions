class School {
    var studentsByGrade = mutableMapOf<Int, MutableSet<String>>()
    
    fun add(student: String, grade: Int) {
        val gradeSet = studentsByGrade.getOrPut(grade) {mutableSetOf<String>()}
        gradeSet.add(student)
    }

    fun grade(grade: Int): List<String> = studentsByGrade[grade]?.sorted() ?: emptyList()

    fun roster(): List<String> = studentsByGrade
            .toSortedMap()
            .flatMap { (grade: Int, students: MutableSet<String>) -> students.sorted() }
}
