import requests

base_url = "https://www.chess.com/"
HEADERS = {
    # "cookie": "visitorid=%3A4a12%3Affff%3A146.0.189.185; asset_push=20181005121800%3Bc62ee%2C4e9d7%2C69d81%2C0805b%2C78184%2C98c4c%2Cc5189%2Cffe3e%2Cba15e%2Ca4531%2C8a3cf; PHPSESSID=64cdfaac6e25590de5e8ec5575fbe133; CHESSCOM_REMEMBERME=Q2hlc3NcV2ViQnVuZGxlXEVudGl0eVxVc2VyOlpHVm1hVzVwZEdWc2VWOXViM1JmWVY5aWIzUT06MTU3MDM2MDkzODpmYzBhZjhmNmViZWIxZDVmMjQ5NDE3ZTRhNTU1ODRmMThlMTNmZmUwZWUwYjI1YWFhZjk2M2U3MDEyOGVjN2I2; amplitude_id_5cc41a1e56d0ee35d4c85d1d4225d2d1chess.com=eyJkZXZpY2VJZCI6ImM4ODQ0YmI0LTZkNWEtNDNhMi05YTZhLWMxMjI5OGJmZDJiN1IiLCJ1c2VySWQiOiI1MDQ2MzcyNiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUzODgyNDkzNTY0NCwibGFzdEV2ZW50VGltZSI6MTUzODgyNDkzNTY0MywiZXZlbnRJZCI6OCwiaWRlbnRpZnlJZCI6MTIsInNlcXVlbmNlTnVtYmVyIjoyMH0=; __cfduid=d691e3d11c61dcee2c9905bd9216003f41538817819; READ_GDPR_POLICY=1; _ga=GA1.2.355511373.1507056872; __gads=ID=cb566503c6ce55c9:T=1507056901:S=ALNI_MbYD2mAq13j84WBgpfwVct88qXvKA"
    "cookie": "visitorid=%3Ac834%3Affff%3A158.64.116.1; PHPSESSID=f7acd3d1662ecf92c6b58f24e9b87f92; CHESSCOM_REMEMBERME=Q2hlc3NcV2ViQnVuZGxlXEVudGl0eVxVc2VyOlpHVm1hVzVwZEdWc2VWOXViM1JmWVY5aWIzUT06MTU3MDYyMjY0NDphZjZmZmU1NmQzOTc1YmFmMGJlMDFmYWFjYWE1ZTMxZGZlMjJmOGY0OWEzNzYxN2VjZjI1NTVkYTM2YjY0NDcx; __cfduid=dcb960ce86578dba18c18b8fc11ce03421539086644; amplitude_id_5cc41a1e56d0ee35d4c85d1d4225d2d1chess.com=eyJkZXZpY2VJZCI6ImViYzhhNWMzLTFlNDEtNGViYy1iMTBiLTg3ODk1NTNjZDQ2NlIiLCJ1c2VySWQiOiI1MDQ2MzcyNiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUzOTA4NjU4MzU1NywibGFzdEV2ZW50VGltZSI6MTUzOTA4NjU4MzU2MiwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjR9; __vrz=1.9.5; __gads=ID=4015140265754660:T=1539086646:S=ALNI_MZXfMwHcQjWoMuQ4qKKt2fSi0QMYw; euconsent=BOVXfnbOVXfnbC6ABAENBt-AAAAh57_______9______9uz_Gv_v_f__33e8__9v_l_7_-___u_-33d4-_1vX99yfm1-7ftr3tp_86ues2_Xur_959__3z0g; crfgL0cSt0r=true; READ_GDPR_POLICY=1; asset_push=20181008135754%3B08afd%2C4e423%2Cb5525%2Ceb085"
}
game_id = ""
is_black = 0

def create_game(user):
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
    print(r.text)


def get_game_json():
    r = requests.get(base_url + "callback/alert/alerts", headers=HEADERS)
    all_games = r.json()["readyGames"]
    game = [game for game in all_games if game["id"] is not game_id]
    if len(game) == 0:
        return
    return game[0]


def get_game_position():
    return get_game_json()["fen"]  # the fen is none when starting position


def get_last_activity():
    return requests.get("https://api.chess.com/int/game/" + game_id).json()[
        "last_activity"]


def get_move_count():
    print(get_game_json()["moveCount"])
    return int(get_game_json()["moveCount"]) * 2 - is_black # -1 if black


def submit_move(move):
    headers = {
        "lastDate": str(get_last_activity()),
        "plyCount": str(get_move_count()),  # opening move of white is 0
        "move": move,
        # "squared": "0",
        # "_token": "ovLEFMwmpgD9D_2_X8zlM1kXQTdgXVDijlqO9HqZG5g"
    }
    print("making move {}".format(move))
    r = requests.post(
        base_url + "callback/game/" + str(game_id) + "/submit-move",
        headers=HEADERS, data=headers)
    print(r.text)


def make_move(notation):
    print("Trying to make move {}".format(notation))
    tile1, tile2 = convert_tile(notation[:2]), convert_tile(notation[2:])
    submit_move(tile1 + tile2)


def convert_tile(tile):
    tiles = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?"
    x, y = "abcdefgh".find(tile[:1]), int(tile[1:]) - 1
    return tiles[y * 8 + x]


def main():
    # create_game("Krecharles")
    # last_activity = get_last_activity(GAME_ID)
    print(get_last_activity())
    print(get_game_position())
    print(submit_move("mu").text)
    print(get_game_position())


if __name__ == '__main__':
    pass
