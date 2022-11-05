from datetime import datetime
import os

######################## COOKIE ###############################
SESSION = []
JWT_USER_SECRET = "e8726d5e-287f-44de-a144-0133e7fa5a4f-6d6a22ae-6dfa-4f95-b27c-f1fa3f451988-7ad4bbef-3133-4a31-8f93-9525e81e9ccd"
JWT_ADMIN_SECRET = "0d9bed44-cd0b-4874-a395-e53c2f905575-8230560f-02af-4eca-8fa5-c31fbbff9226-7f684970-e84f-41e4-bade-ca866476ec5a"

######################## REGEX ###############################
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

######################## UUID ###############################
REGEX_UUID4 = '^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'

######################## USERS ###############################
now = datetime.now()
SIGNUP_DATE = now.strftime('%B %Y')

##### N E W / to add ####
USERS = {
    "a5ea9d0c-1295-4a1e-8184-e22e50ec1914": {
        "user_id": "a5ea9d0c-1295-4a1e-8184-e22e50ec1914",
        "user_first_name": "Aicha",
        "user_last_name": "Haidara",
        "user_name": "AichaHaidara",
        "user_email": "a@a.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "aicha.jpeg",
        "user_signup_date": "January 2014",
        "user_cover_image": "c25.jpg",

        "user_followers": [],
        "user_following": []


    },
    "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6": {
        "user_id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6",
        "user_first_name": "Elisha", 
        "user_last_name": "Ngoma",
        "user_name": "ElishaNgoma",
        "user_email": "a@yahoo.fr", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "elisha.jpg",
        "user_signup_date": "October 2016",
        "user_cover_image": "c10.jpg",

        "user_followers": [],
        "user_following": []
    },
   "0675dae3-bdc8-4638-97d9-bee1c9f47d1b": {
        "user_id": "0675dae3-bdc8-4638-97d9-bee1c9f47d1b",
        "user_first_name": "Kathy",
        "user_last_name": "Wilson",
        "user_name": "KathyWilson",
        "user_email": "aa@a.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p15.jpg",
        "user_signup_date": "May 2013",
        "user_cover_image": "c27.jpg",

        "user_followers": [],
        "user_following": []
    },
    "5413adae-f7fc-42b4-87bb-30eabea9e179": {
        "user_id": "5413adae-f7fc-42b4-87bb-30eabea9e179",
        "user_first_name": "Joseph",
        "user_last_name": "Batts",
        "user_name": "JosephBatts",
        "user_email": "b@b.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p7.jpg",
        "user_signup_date": "February 2016",
        "user_cover_image": "c21.jpg",

        "user_followers": [],
        "user_following": []
    },
    "c2d87430-6c8c-4fa7-b334-be35cebdfe96": {
        "user_id": "c2d87430-6c8c-4fa7-b334-be35cebdfe96",
        "user_first_name": "Robert",
        "user_last_name": "Pan",
        "user_name": "RobertPan",
        "user_email": "c@c.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p9.jpg",
        "user_signup_date": "November 2011",
        "user_cover_image": "c12.jpg",

        "user_followers": [],
        "user_following": []
    },
    "6752541c-2549-490d-9bde-e37fc7b4adb6": {
        "user_id": "6752541c-2549-490d-9bde-e37fc7b4adb6",
        "user_first_name": "Kim",
        "user_last_name": "Mpalo",
        "user_name": "KimMpalo",
        "user_email": "d@d.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p1.jpg",
        "user_signup_date": "March 2012",
        "user_cover_image": "c14.jpg",

        "user_followers": [],
        "user_following": []
    },
    "b48d854c-7e38-43bf-90ea-419a3353fe03": {
        "user_id": "b48d854c-7e38-43bf-90ea-419a3353fe03",
        "user_first_name": "Joseph",
        "user_last_name": "Lan",
        "user_name": "JosephLan",
        "user_email": "e@e.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p2.jpg",
        "user_signup_date": "January 2014",
        "user_cover_image": "c20.jpg",

        "user_followers": [],
        "user_following": []
    },
    "e3120022-44e6-4bf2-ac78-1be9252f98e3": {
        "user_id": "e3120022-44e6-4bf2-ac78-1be9252f98e3",
        "user_first_name": "Margaret",
        "user_last_name": "Sané",
        "user_name": "MargaretSané",
        "user_email": "f@f.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p12.jpg",
        "user_signup_date": "April 2015",
        "user_cover_image": "c5.jpg",

        "user_followers": [],
        "user_following": []
    },
    "35c4038c-ac79-4c4c-9733-e0b21ab7487f": {
        "user_id": "35c4038c-ac79-4c4c-9733-e0b21ab7487f",
        "user_first_name": "Lea",
        "user_last_name": "Komelo",
        "user_name": "LeaKomelo",
        "user_email": "g@g.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p18.jpg",
        "user_signup_date": "August 2019",
        "user_cover_image": "c8.jpg",

        "user_followers": [],
        "user_following": []
    },
    "43a91ef2-49b4-4e82-bd38-c86e9e61b651": {
        "user_id": "43a91ef2-49b4-4e82-bd38-c86e9e61b651",
        "user_first_name": "Antonio",
        "user_last_name": "Ross",
        "user_name": "AntonioRoss",
        "user_email": "h@h.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p20.jpg",
        "user_signup_date": "June 2016",
        "user_cover_image": "c26.jpg",

        "user_followers": [],
        "user_following": []
    },
     "ca4b980d-a92f-4fa7-b127-286f45049c0d": {
        "user_id": "ca4b980d-a92f-4fa7-b127-286f45049c0d",
        "user_first_name": "Hannah",
        "user_last_name": "Stokes",
        "user_name": "HannahStokes",
        "user_email": "i@i.com", 
        "user_password": os.environ.get("USER_PASSORD"),
        "user_profile_picture": "p14.jpg",
        "user_signup_date": "December 2021",
        "user_cover_image": "c6.jpg",

        "user_followers": [],
        "user_following": []
    },
}


ADMIN = {
    "admin_id": os.environ.get('ADMIN_ID'),
    "admin_name": os.environ.get('ADMIN_NAME'),
    "admin_email": os.environ.get('ADMIN_EMAIL'),
    "admin_password": os.environ.get('ADMIN_PASSWORD')
}




######################## TWEETS ###############################

TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 500

now = datetime.now()
TWEET_TIME = now.strftime('%b %d. %H:%M')

TWEETS= {
    "4ffc5ecb-d355-4437-b6b4-6060384ac997": {
        "tweet_id": "4ffc5ecb-d355-4437-b6b4-6060384ac997",
        "user_id": "0675dae3-bdc8-4638-97d9-bee1c9f47d1b",
        "user_first_name": "Kathy",
        "user_last_name": "Wilson",
        "user_name": "KathyWilson",
        "user_profile_picture": "p15.jpg",
        "tweet_text": """Between giant companies getting into NFTs, the constant new 
                obsession with Metaverse, people hawking crypto, whatever the fuck Web3 is, and 
                billionaires having active social media accounts where hundreds line up to kiss 
                the ring, the internet.. kinda sucks right now.""",
        "tweet_image": "t4.jpg",
        "tweet_time": "Jan 01. 12.25",
        "tweet_likes": []
    },
    "21c40e58-9ef8-4457-8923-c627513eb47a": {
        "tweet_id": "21c40e58-9ef8-4457-8923-c627513eb47a",
        "user_id": "5413adae-f7fc-42b4-87bb-30eabea9e179",
        "user_first_name": "Joseph",
        "user_last_name": "Batts",
        "user_name": "JosephBatts",
        "user_profile_picture": "p7.jpg",
        "tweet_text": "u know what pisses me off? the fact that the dark side of the moon is a scam",
        "tweet_image": "t2.jpg",
        "tweet_time": "June 07. 22.14",
        "tweet_likes": []
    },
    "a71c4daf-bdfa-448d-b54c-6a0f18fa8833": {
        "tweet_id": "a71c4daf-bdfa-448d-b54c-6a0f18fa8833",
        "user_id": "c2d87430-6c8c-4fa7-b334-be35cebdfe96",
        "user_first_name": "Robert",
        "user_last_name": "Johnson",
        "user_name": "RobertJohnson",
        "user_profile_picture": "p9.jpg",
        "tweet_text": """Tonight I did a little bit of research into why, 
                    exactly, the U.S. Government has 1.4 BILLION pounds of cheese stored in a 
                    cave deep underneath Springfield, Missouri, & now I’m like “this is a perfect 
                    encapsulation of everything that’s wrong with this country.""",
        "tweet_image": "t12.jpg",
        "tweet_time": "Mar 02. 20.11",
        "tweet_likes": []
    },
    "afca2921-f5bf-4ea6-834a-f60eedb3082b": {
        "tweet_id": "afca2921-f5bf-4ea6-834a-f60eedb3082b",
        "user_id": "6752541c-2549-490d-9bde-e37fc7b4adb6",
        "user_first_name": "Kim",
        "user_last_name": "Mpalo",
        "user_name": "KimMpalo",
        "user_profile_picture": "p1.jpg",
        "tweet_text": """On this final night of 2021, with three hours left on the clock, 
                        I worked extra hard to finish the first draft of my new novel. The story (with all 
                        its current imperfections) is complete! A NYE gift to myself.
                        """,
        "tweet_image": "t10.jpg",
        "tweet_time": "May 12. 21.55",
        "tweet_likes": []
    },
    "487da9be-d8a0-4bd4-aeda-6235f2acd4f6": {
        "tweet_id": "487da9be-d8a0-4bd4-aeda-6235f2acd4f6",
        "user_id": "b48d854c-7e38-43bf-90ea-419a3353fe03",
        "user_first_name": "Joseph",
        "user_last_name": "Holding",
        "user_name": "JosephHolding",
        "user_profile_picture": "p2.jpg",
        "tweet_text": """All you have to do to get this Very Trustworthy Coin is 
                    give us a high resolution scan of your retinas 
                    for the world’s biggest biometrics database!!! 
                    """,
        "tweet_image": "t5.jpg",
        "tweet_time": "Dec 30. 11.00",
        "tweet_likes": []
    },
    "4e714308-8989-4439-8633-31e7630348c4": {
        "tweet_id": "4e714308-8989-4439-8633-31e7630348c4",
        "user_id": "e3120022-44e6-4bf2-ac78-1be9252f98e3",
        "user_first_name": "Margaret",
        "user_last_name": "Doherty",
        "user_name": "MargaretDoherty",
        "user_profile_picture": "p12.jpg",
        "tweet_text": """Web 3 has all the ease of use, simplicity, and friendly 
                developer community of an early Linux device driver connected to your bank account. 
                The only difference is the device driver did something useful if you ever got it to work.""",
        "tweet_image": "t6.jpg",
        "tweet_time": "Sep 04. 08.01",
        "tweet_likes": []
    },
    "1f52ca9d-7355-456e-a525-d269af5a4f15": {
        "tweet_id": "1f52ca9d-7355-456e-a525-d269af5a4f15",
        "user_id": "35c4038c-ac79-4c4c-9733-e0b21ab7487f",
        "user_first_name": "lea",
        "user_last_name": "Komelo",
        "user_name": "LeaKomelo",
        "user_profile_picture": "p18.jpg",
        "tweet_text": """Genuinely surprised this didn't come out of Silicon Valley.  
                    A train that runs on any flat paved surface! I bet you could make these small 
                    enough for a single family to use
                    """,
        "tweet_image": "t13.jpg",
        "tweet_time": "Jan 22. 12.07",
        "tweet_likes": []
    },
    "397edb17-8ab9-41b4-9555-023cc8d93adf": {
        "tweet_id": "397edb17-8ab9-41b4-9555-023cc8d93adf",
        "user_id": "43a91ef2-49b4-4e82-bd38-c86e9e61b651",
        "user_first_name": "Antonio",
        "user_last_name": "Ross",
        "user_name": "AntonioRoss",
        "user_profile_picture": "p20.jpg",
        "tweet_text": """I'm thinking of taking up intermittent feasting. 
                    I heard it can really improve your sleep.
                    """,
        "tweet_image": "t23.jpg",
        "tweet_time": "Jul 03. 17.20",
        "tweet_likes": []
    },
     "266c32e8-36a3-4d95-a9d1-8b9ee470312f": {
        "tweet_id": "266c32e8-36a3-4d95-a9d1-8b9ee470312f",
        "user_id": "ca4b980d-a92f-4fa7-b127-286f45049c0d",
        "user_first_name": "Hannah",
        "user_last_name": "Stokes",
        "user_name": "HannahStokes",
        "user_profile_picture": "p14.jpg",
        "tweet_text": """People making jokes about the Facebook services 
                    going down make me sick. Anyone who was using an Oculus 
                    headset at the time is currently trapped in VR, and if 
                    they die there then they die in real life.
                    """,
        "tweet_image": "t9.jpg",
        "tweet_time": "Aug 19. 09.15",
        "tweet_likes": []
    },


    "baa13631-2b37-4e3d-b86c-5be1beea0217" : {
        "tweet_id": "baa13631-2b37-4e3d-b86c-5be1beea0217",
        "user_id":"a5ea9d0c-1295-4a1e-8184-e22e50ec1914",
        "user_first_name": "Aicha",
        "user_last_name": "Haidara",
        "user_name": "AichaHaidara",
        "user_profile_picture": "aicha.jpeg", 
        "tweet_text": "Look what I have captured, this morining!",
        "tweet_image": "t1.jpg",
        "tweet_time": "Jan 04. 17.15",
        "tweet_likes": []
    }, 
    "cadbbcd7-b569-488c-adbe-adbf4c92b56a": {
        "tweet_id": "cadbbcd7-b569-488c-adbe-adbf4c92b56a",
        "user_id":"b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6", 
        "user_first_name": "Elisha", 
        "user_last_name": "Ngoma",
        "user_name": "ElishaNgoma",
        "user_profile_picture": "elisha.jpg",
        "tweet_text": "Web Development exam is killing me!",
        "tweet_image": "t24.jpg",
        "tweet_time": "Mar 29. 20.30",
        "tweet_likes": []
    },
}

######################## ICONS ###############################

items = [
  {"img":"elisha.jpg", "title":"BBC News", "user_name":"bbcworld"},
  {"img":"dalmatian.jpeg", "title":"Joe Biden", "user_name":"joebiden"},
  {"img":"elisha.jpg", "title":"Vice President", "user_name":"vp"},
  {"img":"elisha.jpg", "title":"Vice President", "user_name":"vp"},
]

tabs = [
  {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home",},
  {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
  {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
  {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
  {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
  {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
  {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
  {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
]

trends = [
  {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
  {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k"},
]