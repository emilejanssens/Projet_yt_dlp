import sys
import os

# Get absolute path to the root of the project
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import re
from code_source.yt_dlp.extractor.vimeo import VimeoIE


class VimeoRegexTest(unittest.TestCase):
    def test_vimeo_regex(self):
        urls = [
            "https://player.vimeo.com/video/54469442",
            "https://player.vimeo.com/video/54469442/",
        ]

        # Test les URL valides
        for valid_urls in urls:
            match = re.match(VimeoIE._VALID_URL, valid_urls)
            self.assertIsNotNone(match, f"The URL {valid_urls} is invalid")

       

if __name__ == '__main__':
    unittest.main()