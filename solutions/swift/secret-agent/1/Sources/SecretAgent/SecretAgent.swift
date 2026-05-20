func protectSecret(_ secret: String, withPassword: String) -> (String) -> String {
  func f(_ password: String) -> String {
    if (withPassword == password) {
      return secret
    } else {
      return "Sorry. No hidden secrets here."
    }
  }
	return f
}

func generateCombination(forRoom room: Int, usingFunction f: (Int) -> Int) -> (Int, Int, Int) {
  (f(room),f(f(room)),f(f(f(room))))
}
