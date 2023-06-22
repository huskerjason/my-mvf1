from datetime import datetime

from mvf1 import MultiViewerForF1

t0 = datetime.now()


def change_player_stream(from_, to_):
    from_ = from_.upper()
    to_ = to_.upper()

    set = {'INTERNATIONAL', 'F1 LIVE', 'TRACKER', 'DATA', 'ZHO', 'BOT', 'DEV', 'TSU', 'OCO', 'GAS', 'ALO', 'STR', 'SAI',
           'LEC', 'MAG', 'HUL', 'NOR', 'PIA', 'RUS', 'HAM', 'VER', 'PER', 'SAR', 'ALB'}

    if to_ not in set or from_ not in set: return False
    t1 = datetime.now()
    print(t1 - t0)

    remote = MultiViewerForF1()
    t1 = datetime.now()
    print(t1 - t0)
    players = remote.players
    t1 = datetime.now()
    print(t1 - t0)

    player_dict = {}
    for p in players:
        splits = str(p).split(': ')
        player_dict[splits[1]] = int(splits[0])

    if from_ not in player_dict.keys(): return False
    t1 = datetime.now()
    print(t1 - t0)

    player = remote.player(player_dict[from_])
    t1 = datetime.now()
    print(t1 - t0)
    player.switch_stream(to_)
    t1 = datetime.now()
    print(t1 - t0)
    remote.player_sync_to_commentary()
    t1 = datetime.now()
    print(t1 - t0)


print(change_player_stream('NOR', 'BOT'))

t1 = datetime.now()
print(t1 - t0)
