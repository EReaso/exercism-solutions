func protectSecret(_ secret: String, withPassword password: String) -> (String) -> String {
  func f(_ MyPassword: String) -> String {
    if (password == MyPassword) {
      return secret
    } else {
      return "Sorry. No hidden secrets here."
    }
  }
	return f
}

func generateCombination(forRoom room: Int, usingFunction f: (Int) -> Int) -> (Int, Int, Int) {
  fatalError("Please implement the generateCombination(forRoom:usingFunction) function")
}
