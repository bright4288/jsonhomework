import json
def set_charact (name):
    character = {
        "name" : name,
        "level" : 1,
        "house" : ["유리집","젤리집","얼음집"],
        "tools" : ["삽","빗자루","청소기"],
        "kind" : ["씨앗","풀","핑크꽃"],
        "skill" : ["물주기","눈발","천둥","햇님"]
    }
    with open("static/game.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    #print ("{0}님 반갑습니다.{1}단계 부터 게임을 시작하겠습니다.".format(character["name"],character["level"]))
    return character

def save_game(filename, charact):
    f = open("filename","w", encoding="utf-8" )
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n"%(key,charact[key]))
    f.close()