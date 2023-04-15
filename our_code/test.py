import sys
import os

# Get absolute path to the root of the project
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import re
from code_source.yt_dlp.extractor.vimeo import VimeoIE


class VimeoRegexTest(unittest.TestCase):
    
    # Define test data as tuples of (regex, url)
    test_data = [
        ("https://player.vimeo.com/video/54469442", VimeoIE._VALID_URL),
        ("https://player.vimeo.com/video/54469442/", VimeoIE._VALID_URL),
        
    ]
    
    def test_regex(self): 
        for url, regex in self.test_data:
            with self.subTest(url=url):
                match = re.match(regex, url)
                self.assertIsNotNone(match, f"The URL {url} is invalid")


    
if __name__ == '__main__':
    unittest.main()