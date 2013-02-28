import price
import unittest

class TestPrice(unittest.TestCase):

	def setUp(self):
		self.raw_to_parsed = { 
				"1.00": Price(1),
				"R$1,99": Price(1, 99),
				"R$500": Price(500),
				"R $412,53": Price(412, 53),
				"U$ 530.50": Price(530, 50),
				"R$ 12 0,2 5": Price(120, 25),
				"R$ 7021 , 09": Price(7012, 9),
				"Ih R$ 1 acho 2%q 3, bugo0u5": Price(123, 5),
				"Apenas R $2 9, 0 0": Price(29),
				"Tá caro? Promoção: só R$ 1 9 9 , 9 9 reais": Price(199, 99),
				"Châteu La Croix de Queynac 2009 Rouge 5.90 €/bouteille": Price(5, 90),
				"Apenas 4 reais!": Price(4),
				"Uncroyable! Côtes de Blaye: 4. 8 0 € au lieu de 14,90€ !": [Price(4, 80), Price(14, 90)]}

	def test_parsing(self):
		for r in raw_to_parsed.keys():
			p = parse_price(r)
			self.assertEqual(p, raw_to_parsed[r])

if __name__ == '__main__':
	unittest.main()
