import unittest


class BubbleSort(unittest.TestCase):

    def test_for_functionality1(self):
        self.assertEqual(caesar_cipher("Boy! What a string!", -5), "Wjt! Rcvo v nomdib!")

    def test_for_functionality2(self):
        self.assertEqual(caesar_cipher("Hello zach168! Yes here.", 5), "Mjqqt efhm168! Djx mjwj.")

    def test_for_functionality3(self):
        self.assertEqual(caesar_cipher("Hello Zach168! Yes here.", -5), "Czggj Uvxc168! Tzn czmz.")
    
if __name__ == '__main__':
    unittest.main()