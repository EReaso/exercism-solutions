func dailyRateFrom(hourlyRate: Double) -> Double {
	hourlyRate*8
}

func monthlyRateFrom(hourlyRate: Double, withDiscount: Double) -> Double {
	dailyRateFrom(hourlyRate: hourlyRate)*22/(withDiscount/100)
}

func workdaysIn(budget: Double, hourlyRate: Double, withDiscount: Double) -> Double {
	budget/(dailyRateFrom(hourlyRate: hourlyRate))/(withDiscount/100)
}
