func canIBuy(vehicle: String, price: Double, monthlyBudget: Double) -> String {
  if monthlyBudget >= price / 60 {
    "Yes! I'm getting a \(vehicle)"
  } else if monthlyBudget * 1.1 >= price / 60 {
    "I'll have to be frugal if I want a \(vehicle)"
  } else {
    "Darn! No \(vehicle) for me"
  }
}

func licenseType(numberOfWheels wheels: Int) -> String {
  if wheels == 2 || wheels == 3 {
    "You will need a motorcycle license for your vehicle"
  } else if wheels == 4 || wheels == 6 {
    "You will need an automobile license for your vehicle"
  } else if wheels == 18 {
    "You will need a commercial trucking license for your vehicle"
  } else {
    "We do not issue licenses for those types of vehicles"
  }
}

func calculateResellPrice(originalPrice: Double, yearsOld: Int) -> Double {
  if yearsOld < 3 {
	originalPrice * 0.7
  } else if yearsOld >= 10 {
	originalPrice * 0.5
  } else {
	originalPrice * 0.7
  }
}
