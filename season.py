# TODO: Replace stub w/ util that either
# 1. Freshly calls an LLM
# 2. Gets from cache Country, Season, and Recommendations if alr exist


COUNTRY_SEASON_RECOS_MAP = {
    "South Korea": {
        "Spring": [
            "Cherry Blossom Viewing in Seoul and Gyeongju",
            "Hiking in Seoraksan National Park",
            "Visiting Historical Palaces like Gyeongbokgung",
            "Participating in Buddha's Birthday Celebrations",
            "Exploring Spring Flower Festivals"
        ],
        "Summer": [
            "Beach Getaways to Busan and Jeju Island",
            "Water Sports at South Korea's Coastal Areas",
            "Exploring Jeju's Lava Tubes and Waterfalls",
            "Enjoying Korean Bingsu (Shaved Ice Dessert)",
            "Participating in Mud Festivals"
        ],
        "Fall": [
            "Hiking in Naejangsan National Park for Fall Foliage",
            "Tasting Fresh Apples in the Countryside",
            "Exploring Korean Traditional Markets",
            "Participating in Chuseok (Korean Thanksgiving) Festivities",
            "Taking Scenic Autumn Drives"
        ],
        "Winter": [
            "Skiing and Snowboarding in the Korean Alps",
            "Ice Skating in Seoul's Outdoor Rinks",
            "Visiting Winter Festivals like the Hwacheon Sancheoneo Ice Festival",
            "Sampling Delicious Korean Winter Street Food",
            "Relaxing in Korean Saunas (Jjimjilbang)"
        ]
    },
    "Philippines": {
        "Dry Season": [
            "Beach Holidays in Boracay, Palawan, and Cebu",
            "Scuba Diving and Snorkeling in Tubbataha Reefs Natural Park",
            "Exploring Underground Rivers in Puerto Princesa",
            "Festivals like Sinulog in Cebu",
            "Trekking in Banaue Rice Terraces"
        ],
        "Rainy Season": [
            "Surfing in Siargao",
            "Whale Watching in Donsol",
            "Enjoying Hot Soups and Comfort Food",
            "Visiting Waterfalls in Mindanao and Luzon",
            "Experiencing Kadayawan Festival in Davao"
        ],
        "Cool Season": [
            "Hiking and Trekking in the Cordillera Mountains",
            "Participating in the Pahiyas Festival in Lucban",
            "Exploring Historical Sites in Manila",
            "Sampling Filipino Christmas Delicacies",
            "Visiting Bicolandia's Natural Wonders"
        ]
    },
    "Taiwan": {
        "Spring": [
            "Cherry Blossom Viewing in Yangmingshan National Park",
            "Exploring Taroko Gorge's Stunning Landscapes",
            "Visiting Traditional Temples and Festivals",
            "Hiking in Alishan National Scenic Area",
            "Experiencing Songkran Festival in Taipei"
        ],
        "Summer": [
            "Beach Trips to Kenting and Green Island",
            "Water Sports like Surfing and Scuba Diving",
            "Night Market Food Adventures",
            "Attending Dragon Boat Festivals",
            "Exploring the Penghu Islands"
        ],
        "Fall": [
            "Hiking Amidst Autumn Foliage in Taichung",
            "Enjoying Sun Moon Lake Scenic Views",
            "Experiencing the Mid-Autumn Festival",
            "Visiting Historic Sites like Chiang Kai-shek Memorial Hall",
            "Exploring Jiufen's Old Streets"
        ],
        "Winter": [
            "Hot Spring Retreats in Beitou and Wulai",
            "Exploring Taipei's Street Food Scene",
            "Snow and Ice Festivals in Yilan",
            "Participating in Chinese New Year Celebrations",
            "Visiting the National Palace Museum"
        ]
    }
}


def get_seasons(country: str, season: str):
    result_season = None
    result_options = []

    season = season.title()

    country_data = COUNTRY_SEASON_RECOS_MAP.get(country, None)
    country_seasons = [season for season in country_data.keys()]
    if season not in country_seasons:
        result_options = country_seasons
    else:
        result_season = season

    return (result_season, result_options)


def get_recommendations(country: str, season: str):
    return COUNTRY_SEASON_RECOS_MAP[country][season]
