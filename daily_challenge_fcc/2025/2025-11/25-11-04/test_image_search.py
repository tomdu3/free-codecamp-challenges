import unittest
from image_search import image_search

class TestImageSearch(unittest.TestCase):
    
    def test_basic_dog_search(self):
        self.assertEqual(image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"), ["dog.png"])
        
    def test_sun_related_search(self):
        self.assertEqual(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"), 
                        ["Sunset.jpg", "sunflower.jpeg"])
        
    def test_extension_search(self):
        self.assertEqual(image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG"),
                        ["Moon.png", "stars.png"])
        
    def test_cat_related_search(self):
        self.assertEqual(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", 
                                     "catNip.jpeg", "franken_cat.gif"], "Cat"),
                        ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"])
        
    def test_empty_list(self):
        self.assertEqual(image_search([], "test"), [])
        
    def test_no_matches(self):
        self.assertEqual(image_search(["dog.jpg", "cat.png"], "bird"), [])
        
    def test_case_sensitivity(self):
        self.assertEqual(image_search(["DOG.jpg", "Dog.png", "dog.jpeg"], "dog"),
                        ["DOG.jpg", "Dog.png", "dog.jpeg"])
        
    def test_special_characters(self):
        self.assertEqual(image_search(["test-image.jpg", "test_image.png"], "-"),
                        ["test-image.jpg"])

if __name__ == '__main__':
    unittest.main()