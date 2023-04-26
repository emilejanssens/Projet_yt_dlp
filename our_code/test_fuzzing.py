import subprocess

# Valid inputs
inputs = [
    "https://www.youtube.com/watch?v=pRpeEdMmmQ0",
    "https://www.youtube.com/watch?v=F_mqShCzlAY",
    "https://www.youtube.com/watchv=F_mqShCzlAY",
    'https://www.youtube.com/watch?v=F_mqShCzlAY"&"list=PLhQjrBD2T382hjVvKtTiBQYvDxGDQyU4p',
    "https://player.vimeo.com/video/54469442",
    "https://player.vimeo.com/video/54469442/",
    
    "https://watch.pokemon.com/fr-fr/#/player?id=c0d71edb6ec243ae94718327637ac46c/",
    "https://watch.pokemon.com/fr-fr/#/player?id=c0d71edb6ec243ae94718327637ac46c/test",
    "https://watch.pokemon.com/fr-fr/#/player?id=c0d71edb6ec243ae94718327637ac46c",

    "https://www.instagram.com/stories/hugodecrypte/3080791283912358444/",
    "https://www.instagram.com/stories/hugodecrypte/3080791283912358444",
    "https://www.instagram.com/stories/hugodecrypte/3080791283912358444/test",
    "https://www.instagram.com/p/Cpk_IWlDt21/",
    "https://www.instagram.com/p/Cpk_IWlDt21",
    "https://www.instagram.com/p/Cpk_IWlDt21/test",

    "https://www.facebook.com/fcbarcelona/videos/182599291408939",
    "https://www.facebook.com/fcbarcelona/videos/182599291408939/",
    "https://www.facebook.com/fcbarcelona/videos/182599291408939/test",
    "https://www.facebook.com/watch/?v=1363029404119602",
    "https://www.facebook.com/watch/?v=1363029404119602/",
    "https://www.facebook.com/reel/1195014674539147/?s=single_unit",
    "https://www.facebook.com/reel/1195014674539147/?s=single_unit/",

    "https://www.dailymotion.com/video/x8k2sh7?playlist=x6bgai",
    "https://www.dailymotion.com/video/x8k2sh7?playlist=x6bgai/",
    "https://www.dailymotion.com/video/x8k1mpj",
    "https://www.dailymotion.com/video/x8k1mpj/",

    "https://www.formula1.com/en/latest/video.in-depth-sergio-perez-reflects-on-his-time-with-racing-point.1687525282173377683.html",
    "https://www.formula1.com/en/latest/video.in-depth-sergio-perez-reflects-on-his-time-with-racing-point.1687525282173377683.html/",

    "https://www.nintendo.com/nintendo-direct/03-09-2023/",
    "https://www.nintendo.com/nintendo-direct/03-09-2023",

    # erreur susceptible de Facebook
    "https://m.facebook.com/stories/view_tray_pagination/1694351550654428/?tray_session_id=f3f6199a-d2d4-4d88-9906-1a47834e22f1&thread_id=782399996346255&end_cursor=MTAwMDA5NzcwNjQ5NTQyOjE6MTY4MTU1NTM5MDoxNjg3MTY5Njc5NTQzODE6LTE6Y2xuOjI5OTc0MjQwOTA5NjA0MTc4NTM6MDoxNjgxNTU1MzkwOg%3D%3D&has_next_page=false",

    "https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT/view/",
    "https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT/view",
    "https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT/youyou",
    "https://drive.google.com/file/d/1BiLl5grkxDNXVUvkBJanA-0d_Q0sfUBT",

    "https://www.tiktok.com/@reussironly/video/7221968120259366150?is_from_webapp=1&sender_device=pc",
    "https://www.tiktok.com/@reussironly/video/7221968120259366150a",
    "https://www.tiktok.com/@reussironly/video/7221968120259366150/",

    "https://www.deezer.com/fr/album/350891827",
    "https://www.deezer.com/fr/album/350891827/",
    "https://www.deezer.com/XX/album/350891827",
    "https://www.deezer.com////album/350891827",
    "https://www.deezer.com/fr/playlist/10783752422",
    "https://www.deezer.com/&#/playlist/10783752422",
    "https://www.deezer.com/fr/playlist/10783752422/",

    "https://www.amazon.aaa.bb/dp/B098XNCHLD/?th=1",
    "https://www.amazon.aaa.bb/dp/B098XNCHLD###&&&",
    "https://www.amazon.com/gp/customer-reviews/R10VE9VUSY19L3/ref=cm_cr_arp_d_rvw_ttl",
    "https://www.amazon.com/gp/customer-reviews/R10VE9VUSY19L3##&&",

    "https://www.reddit.com/r/interestingasfuck/comments/12mjhdz/worst_pain_known_to_man/",
    "https://www.reddit.com/r/interestingasfuck/comments/12mjhdz#",

    # erreur eurosport
    "https://www.eurosport.com/football/champions-league/2022-2023/pep-guardiola-emotionally-destroyed-after-manchester-city-win-over-bayern-munich-in-champions-league_vid1896254/video.shtml",
    "https://www.eurosport.com/football/champions-league/20222023/pep-guardiola-emotionally-destroyed-after-manchester-city-win-over-bayern-munich-in-champions-league_vid1896254",

    "https://youtu.be/dQw4w9WgXcQ",
    "https://www.youtube.com/live/dQw4w9WgXcQ",
    "https://www.youtube-nocookie.com/watch?v=dQw4w9WgXcQ",
    "https://www.deturl.com/www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.deturl.com/www.youtube.com/watch?v=dQw4w9WgXcQ/",
    "https://www.pwnyoutube.com/watch?v=dQw4w9WgXcQ",

    "https://www.invidio.us/playlist?list=PLVhZRy5c_nYhLrjji-jYZyKrNmOy8QvD-",
    "https://mychannel.youtube.com/playlist?list=PLvahj0XJXycFCQ-27Y6UYYv6JdK0hNZrB/",
    "https://www.youtube.com/playlist?list=PLvahj0XJXycFCQ-27Y6UYYv6JdK0hNZrB",

    "https://www.youtube.com/results?search_query=example",
    "https://youtube.com/search?search_query=example&lang=en",
    "https://www.youtube.com/results?search_query=example&lang=en/s",

    "https://music.youtube.com/search?search_query=example&ytsession=bVn1nETu68jVrEzZcdjb7pWiBoNoGmta",
    "https://music.youtube.com/search?search_query=example&ab_channel=exampleChannel",
    "http://music.youtube.com/search?q=example/"
]

COMMAND = "yt-dlp {} -P ./trash"

for input_str in inputs:
    try:
        output = subprocess.check_output(COMMAND.format(
            input_str), shell=True, stderr=subprocess.STDOUT)
        print(f"Command succeeded with input: {input_str}")
        # print(output)

    except subprocess.CalledProcessError as e:

        print(f"Command failed with input: {input_str}")
        print(e.output)
