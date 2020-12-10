# Goal: 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질
# 때, 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return
# 하도록 solution 함수를 완성하라.

# 제한사항
#   record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
#   다음은 record에 담긴 문자열에 대한 설명이다.
#   모든 유저는 [유저 아이디]로 구분한다.
#   [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - Enter [유저 아이디] [닉네임] (ex. Enter uid1234 Muzi)
#   [유저 아이디] 사용자가 채팅방에서 퇴장 - Leave [유저 아이디] (ex. Leave uid1234)
#   [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - Change [유저 아이디] [닉네임] (ex. Change uid1234 Muzi)
#   첫 단어는 Enter, Leave, Change 중 하나이다.
#   각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
#   유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
#   유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
#   채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.

# Example
#   1) ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#      ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

#      ["Enter uid1234 Muzi"] --> {"uid1234": "Muzi"}
#      ["Enter uid1234 Muzi", Enter uid4567 Prodo] --> {"uid1234": "Muzi", "uid4567": "Prodo"}
#      ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234"] --> {"uid1234": "Muzi", "uid4567": "Prodo"}
#      ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo"] --> {"uid1234": "Prodo", "uid4567": "Prodo"}
#      ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"] --> {"uid1234": "Prodo", "uid4567": "Ryan"}


#      ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# Pseudocode
#   from record store usernames by id
#   for each record
#       parse by space in item
#       if item[0] has Enter, create string "____님이 들어왔습니다"
#       if item[0] has Leave, create string "____님이 나갔습니다"
#       if item[0] has Change, skip"
#       append string to answer

#   return answer

def solution(record):
    answer = []

    # from record store usernames by id
    nicknames = store_nicknames(record)

    # for each record
    for item in record:
        msg = ""

        # parse by space in item
        item = item.split(" ")
        id = item[1]
        # if item[0] has Enter, create string "____님이 들어왔습니다"
        if item[0] == "Enter":
            msg = "{}님이 들어왔습니다".format(nicknames[id])
        # if item[0] has Leave, create string "____님이 나갔습니다"
        elif item[0] == "Leave":
            msg = "{}님이 나갔습니다".format(nicknames[id])
        # if item[0] has Change, skip"
        else:
            continue
        # append string to answer
        answer.append(msg)

    # return answer
    return answer

def store_nicknames(record):
    res = {}




    return res

