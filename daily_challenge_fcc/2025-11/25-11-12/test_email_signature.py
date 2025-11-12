import unittest
from email_signature import generate_signature

class TestGenerateSignature(unittest.TestCase):
    def test_quinn_waverly(self):
        self.assertEqual(
            generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"),
            "--Quinn Waverly, Founder and CEO at TechCo"
        )

    def test_alice_reed(self):
        self.assertEqual(
            generate_signature("Alice Reed", "Engineer", "TechCo"),
            ">>Alice Reed, Engineer at TechCo"
        )

    def test_tina_vaughn(self):
        self.assertEqual(
            generate_signature("Tina Vaughn", "Developer", "example.com"),
            "::Tina Vaughn, Developer at example.com"
        )

    def test_b_b(self):
        self.assertEqual(
            generate_signature("B. B.", "Product Tester", "AcmeCorp"),
            ">>B. B., Product Tester at AcmeCorp"
        )

    def test_windstorm(self):
        self.assertEqual(
            generate_signature("windstorm", "Cloud Architect", "Atmospheronics"),
            "::windstorm, Cloud Architect at Atmospheronics"
        )

if __name__ == "__main__":
    unittest.main()