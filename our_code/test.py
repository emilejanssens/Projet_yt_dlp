import sys
import os

# Get absolute path to the root of the project
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import re
from code_source.yt_dlp.extractor.vimeo import VimeoIE
from code_source.yt_dlp.extractor.pokemon import PokemonWatchIE
from code_source.yt_dlp.extractor.instagram import InstagramIE, InstagramStoryIE
from code_source.yt_dlp.extractor.facebook import FacebookIE, FacebookReelIE
from code_source.yt_dlp.extractor.dailymotion import DailymotionIE
from code_source.yt_dlp.extractor.formula1 import Formula1IE
from code_source.yt_dlp.extractor.nintendo import NintendoIE
from code_source.yt_dlp.extractor.googledrive import GoogleDriveIE
from code_source.yt_dlp.extractor.reddit import RedditIE
from code_source.yt_dlp.extractor.tiktok import TikTokIE
from code_source.yt_dlp.extractor.deezer import DeezerAlbumIE,DeezerPlaylistIE
from code_source.yt_dlp.extractor.amazon import AmazonStoreIE,AmazonReviewsIE
from code_source.yt_dlp.extractor.eurosport import EurosportIE


class VimeoRegexTest(unittest.TestCase):
    
    # Define test data as tuples of (regex, url)
    test_data = [
        ("https://player.vimeo.com/video/54469442", VimeoIE._VALID_URL),
        ("https://player.vimeo.com/video/54469442/", VimeoIE._VALID_URL),
        ("https://watch.pokemon.com/fr-fr/#/player?id=c0d71edb6ec243ae94718327637ac46c/", PokemonWatchIE._VALID_URL),
        ("https://watch.pokemon.com/fr-fr/#/player?id=c0d71edb6ec243ae94718327637ac46c/test", PokemonWatchIE._VALID_URL),
        ("https://watch.pokemon.com/fr-fr/#/player?id=c0d71edb6ec243ae94718327637ac46c", PokemonWatchIE._VALID_URL),
        ("https://www.instagram.com/stories/hugodecrypte/3080791283912358444/", InstagramStoryIE._VALID_URL),
        ("https://www.instagram.com/stories/hugodecrypte/3080791283912358444", InstagramStoryIE._VALID_URL),
        ("https://www.instagram.com/stories/hugodecrypte/3080791283912358444/test", InstagramStoryIE._VALID_URL),
        ("https://www.instagram.com/p/Cpk_IWlDt21/", InstagramIE._VALID_URL),
        ("https://www.instagram.com/p/Cpk_IWlDt21", InstagramIE._VALID_URL),
        ("https://www.instagram.com/p/Cpk_IWlDt21/test", InstagramIE._VALID_URL),
        ("https://www.facebook.com/fcbarcelona/videos/182599291408939", FacebookIE._VALID_URL),
        ("https://www.facebook.com/fcbarcelona/videos/182599291408939/", FacebookIE._VALID_URL),
        ("https://www.facebook.com/fcbarcelona/videos/182599291408939/test", FacebookIE._VALID_URL),
        ("https://www.facebook.com/watch/?v=1363029404119602", FacebookIE._VALID_URL),
        ("https://www.facebook.com/watch/?v=1363029404119602/", FacebookIE._VALID_URL),
        ("https://www.facebook.com/reel/1195014674539147/?s=single_unit", FacebookReelIE._VALID_URL),
        ("https://www.facebook.com/reel/1195014674539147/?s=single_unit/", FacebookReelIE._VALID_URL),
        ("https://www.dailymotion.com/video/x8k2sh7?playlist=x6bgai", DailymotionIE._VALID_URL),
        ("https://www.dailymotion.com/video/x8k2sh7?playlist=x6bgai/", DailymotionIE._VALID_URL),
        ("https://www.dailymotion.com/video/x8k1mpj", DailymotionIE._VALID_URL),
        ("https://www.dailymotion.com/video/x8k1mpj/", DailymotionIE._VALID_URL),
        ("https://www.formula1.com/en/latest/video.in-depth-sergio-perez-reflects-on-his-time-with-racing-point.1687525282173377683.html", Formula1IE._VALID_URL),
        ("https://www.formula1.com/en/latest/video.in-depth-sergio-perez-reflects-on-his-time-with-racing-point.1687525282173377683.html/", Formula1IE._VALID_URL),
        ("https://www.nintendo.com/nintendo-direct/03-09-2023/", NintendoIE._VALID_URL),
        ("https://www.nintendo.com/nintendo-direct/03-09-2023", NintendoIE._VALID_URL),
        # erreur susceptible de Facebook
        ("https://m.facebook.com/stories/view_tray_pagination/1694351550654428/?tray_session_id=f3f6199a-d2d4-4d88-9906-1a47834e22f1&thread_id=782399996346255&end_cursor=MTAwMDA5NzcwNjQ5NTQyOjE6MTY4MTU1NTM5MDoxNjg3MTY5Njc5NTQzODE6LTE6Y2xuOjI5OTc0MjQwOTA5NjA0MTc4NTM6MDoxNjgxNTU1MzkwOg%3D%3D&has_next_page=false", FacebookIE._VALID_URL),
        ("https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT/view/",GoogleDriveIE._VALID_URL),
        ("https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT/view",GoogleDriveIE._VALID_URL),
        ("https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT/youyou",GoogleDriveIE._VALID_URL),
        ("https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT",GoogleDriveIE._VALID_URL),
        ("https://www.tiktok.com/@reussironly/video/7221968120259366150?is_from_webapp=1&sender_device=pc",TikTokIE._VALID_URL),
        ("https://www.tiktok.com/@reussironly/video/7221968120259366150a",TikTokIE._VALID_URL),
        ("https://www.tiktok.com/@reussironly/video/7221968120259366150/",TikTokIE._VALID_URL),
        ("https://www.deezer.com/fr/album/350891827",DeezerAlbumIE._VALID_URL),
        ("https://www.deezer.com/fr/album/350891827/",DeezerAlbumIE._VALID_URL),
        ("https://www.deezer.com/XX/album/350891827",DeezerAlbumIE._VALID_URL),
        ("https://www.deezer.com////album/350891827",DeezerAlbumIE._VALID_URL),
        ("https://www.deezer.com/fr/playlist/10783752422",DeezerPlaylistIE._VALID_URL),
        ("https://www.deezer.com/&#/playlist/10783752422",DeezerPlaylistIE._VALID_URL),
        ("https://www.deezer.com/fr/playlist/10783752422/",DeezerPlaylistIE._VALID_URL),
        ("https://www.amazon.aaa.bb/dp/B098XNCHLD/?th=1",AmazonStoreIE._VALID_URL),
        ("https://www.amazon.aaa.bb/dp/B098XNCHLD###&&&",AmazonStoreIE._VALID_URL),
        ("https://www.amazon.com/gp/customer-reviews/R10VE9VUSY19L3/ref=cm_cr_arp_d_rvw_ttl",AmazonReviewsIE._VALID_URL),
        ("https://www.amazon.com/gp/customer-reviews/R10VE9VUSY19L3##&&",AmazonReviewsIE._VALID_URL),
        ("https://www.reddit.com/r/interestingasfuck/comments/12mjhdz/worst_pain_known_to_man/",RedditIE._VALID_URL),
        ("https://www.reddit.com/r/interestingasfuck/comments/12mjhdz#",RedditIE._VALID_URL),
        #erreur eurosport
        ("https://www.eurosport.com/football/champions-league/2022-2023/pep-guardiola-emotionally-destroyed-after-manchester-city-win-over-bayern-munich-in-champions-league_vid1896254/video.shtml",EurosportIE._VALID_URL),
        ("https://www.eurosport.com/football/champions-league/20222023/pep-guardiola-emotionally-destroyed-after-manchester-city-win-over-bayern-munich-in-champions-league_vid1896254",EurosportIE._VALID_URL),
    ]
    
    def test_regex(self): 
        for url, regex in self.test_data:
            with self.subTest(url=url):
                match = re.match(regex, url)
                self.assertIsNotNone(match, f"The URL {url} is invalid")


    
if __name__ == '__main__':
    unittest.main()