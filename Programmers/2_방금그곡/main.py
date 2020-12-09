# goal: 네오가 찾으려는 음악의 제목을 구하여라

# 입력 형식
#   - 입력으로 네오가 기억한 멜로디를 담은 문자열 m과 방송된 곡의 정보를 담고 있는 배열 musicinfos가 주어진다.
#
#   - m은 음 1개 이상 1439개 이하로 구성되어 있다.
#   - musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
#   - 음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
#   - 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
#   - 악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.

# Example
#   1) m: ABCDEFG   musicinfos: ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
#       - CDEFG in musicinfos[0], length 14 seconds
#       - ABCDE in musicinfos[1], length 5 seconds
#       - Choose musicinfos[0]

#   2) m: CC#BCC#BCC#BCC#B  musicinfos: ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
#       - CC#B in musicinfos[0], length 30 seconds
#       - CC#BCC#BCC#B in musicinfos[1], length 8 seconds
#       - Choose musicinfos[0]

#   3) m: ABC  musicinfos: ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
#       - None in musicinfos[0], length 14 seconds
#       - ABC in musicinfos[1], length 5 seconds
#       - Choose musicinfos[1]

# Cases
#   1. when len(m) > len(musicinfos[i]) (e.g. CDEFGAB)

# Pseudocode
#   - for each musicinfo,
#       Parse string to time_start, time_end, name, m_music
#       Calculate duration
#       for each substring of decreasing size in m, check if the substring exists n m_music
#           if exists and has higher duration, record name, duration and continue

#   return name

import datetime
def solution(m, musicinfos):
    answer = ''

    # for each musicinfo,
    for info in musicinfos:
        # Parse string to time_start, time_end, name, m_music
        time_start, time_end, name, m_music = info.split(",")
        # calculate duration
        duration = (datetime.strptime(time_end, "%H:%M") - datetime.strptime(time_start, "%H:%M")).seconds
        # for each substring of decreasing size in m, check if the substring exists n m_music
        # if exists and has higher duration, record name, duration and continue
    return answer