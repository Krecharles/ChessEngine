import requests

base_url = "https://www.chess.com/"
HEADERS = {
    "cookie": "visitorid=%3Ac834%3Affff%3A158.64.116.1; PHPSESSID=f7acd3d1662ecf92c6b58f24e9b87f92; CHESSCOM_REMEMBERME=Q2hlc3NcV2ViQnVuZGxlXEVudGl0eVxVc2VyOlpHVm1hVzVwZEdWc2VWOXViM1JmWVY5aWIzUT06MTU3MDYyMjY0NDphZjZmZmU1NmQzOTc1YmFmMGJlMDFmYWFjYWE1ZTMxZGZlMjJmOGY0OWEzNzYxN2VjZjI1NTVkYTM2YjY0NDcx; __cfduid=dcb960ce86578dba18c18b8fc11ce03421539086644; amplitude_id_5cc41a1e56d0ee35d4c85d1d4225d2d1chess.com=eyJkZXZpY2VJZCI6ImViYzhhNWMzLTFlNDEtNGViYy1iMTBiLTg3ODk1NTNjZDQ2NlIiLCJ1c2VySWQiOiI1MDQ2MzcyNiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUzOTA4NjU4MzU1NywibGFzdEV2ZW50VGltZSI6MTUzOTA4NjU4MzU2MiwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjR9; __vrz=1.9.5; __gads=ID=4015140265754660:T=1539086646:S=ALNI_MZXfMwHcQjWoMuQ4qKKt2fSi0QMYw; euconsent=BOVXfnbOVXfnbC6ABAENBt-AAAAh57_______9______9uz_Gv_v_f__33e8__9v_l_7_-___u_-33d4-_1vX99yfm1-7ftr3tp_86ues2_Xur_959__3z0g; crfgL0cSt0r=true; READ_GDPR_POLICY=1; asset_push=20181008135754%3B08afd%2C4e423%2Cb5525%2Ceb085"
}


def create_game_against_user(user):
    body = {
        "gameType": "chess",
        "daysPerMove": "14",
        "color": "0",
        "takeback": "1",
        "minRequiredGameCount": "0",
        "maxTimeoutPercent": "100",
        "minMembershipLevel": "10",
        "isRated": "0"
    }
    r = requests.post(base_url + "callback/game/daily/challenge/" + user,
                      headers=HEADERS, data=body)
    return r.text


def create_game():
    params = {
        "_token": "WqtE3l_AOPtf1eEwtYn7lsEvSd0_esmbplOKbsmJF2I",
        "minGamesPlayed": 0,
        # "opponent": null,
        "isRated": 1,
        "takeback": 0,
        "minRequiredGameCount": 0,
        "maxTimeoutPercent": 100,
        "minMembershipLevel": 10,
        "gameType": "chess",
        "daysPerMove": 1,
        "color": "0",
        "rating": {
            "minRatingDelta": -200,
            "maxRatingDelta": 200
        },
        "minRatingDelta": 200,
        "maxRatingDelta": 200
    }
    r = requests.post(
        "https://www.chess.com/callback/game/random/daily/challenge",
        headers=HEADERS, data=params)
    res = r.json()
    print("[CREATING GAME]: {}".format(res["message"]))

def get_all_games():
    r = requests.get(base_url + "callback/alert/alerts", headers=HEADERS)
    return r.json()["readyGames"]


def get_last_activity(game_id):
    return \
    requests.get("https://api.chess.com/int/game/" + str(game_id)).json()[
        "last_activity"]


def submit_move(game, move):
    play_count = game["moveCount"] * 2
    if game["flipBoard"]:
        play_count -= 1
    headers = {
        "lastDate": str(get_last_activity(game["id"])),
        "plyCount": str(play_count),  # opening move of white is 0
        "move": move,
        # "squared": "0",
        # "_token": "ovLEFMwmpgD9D_2_X8zlM1kXQTdgXVDijlqO9HqZG5g"
    }
    print("Playing {} on game with id {} on move {}".format(move, game["id"],
                                                            play_count))
    r = requests.post(
        base_url + "callback/game/" + str(game["id"]) + "/submit-move",
        headers=HEADERS, data=headers)
    # print(r.text)


def make_move(game, notation):
    tile1, tile2 = convert_tile(notation[:2]), convert_tile(notation[2:])
    submit_move(game, tile1 + tile2)


def convert_tile(tile):
    tiles = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?"
    x, y = "abcdefgh".find(tile[:1]), int(tile[1:2]) - 1
    return tiles[y * 8 + x]

# def main():
# create_game("Krecharles")
# last_activity = get_last_activity(GAME_ID)
