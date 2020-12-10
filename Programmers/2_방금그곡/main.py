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
#   1. 음악 길이보다 재생된 시간이 길 때
#   2. 음악 길이보다 재생된 시간이 짧을 때

# Pseudocode
#   split m to list of substrings to use in search
#   for each musicinfo,
#       Parse string to time_start, time_end, name, m_music
#       Calculate duration
#       for each substring of decreasing size in m, check if the substring exists n m_music
#           if 음악 길이보다 재생된 시간이 길 때
#               extend m_music to match m
#               check if m in extended m_music
#           if 음악 길이보다 재생된 시간이 짧을 때
#               check if m in extended m_music
#   return name

from datetime import datetime
import math

def solution(m, musicinfos):
    answer = ''
    m = replace_sharps(m)

    highest_duration = -1

    # for each musicinfo,
    for info in musicinfos:
        # Parse string to time_start, time_end, name, m_music
        time_start, time_end, name, m_music = info.split(",")
        # replace sharps
        m_music = replace_sharps(m_music)
        # calculate duration
        duration = (datetime.strptime(time_end, "%H:%M") - datetime.strptime(time_start, "%H:%M")).seconds // 60

        m_music = extend_m_music(m_music, m, duration)

        # check if m in extended m_music
        # if exists and has higher duration, record name, duration and continue
        if m in m_music:
            answer = name if duration > highest_duration else answer
            highest_duration = max(duration, highest_duration)


    if highest_duration < 0:
        return "(None)"
    else:
        return answer

def replace_sharps(m):
    sharps = ["C#", "D#", "F#", "G#", "A#"]
    N = len(m)

    if N == 1:
        return m

    for index, sharp in enumerate(sharps):
        m = m.replace(sharp, str(index))

    return m

def extend_m_music(m_music, m, duration):
    res = ""
    N_m_music = len(m_music)
    N_m = len(m)

    res = m_music * duration
    res = res[:duration+1]

    return res

if __name__ == "__main__":
    print(solution("ABC", ["12:00,12:14,HELLO,DEF", "13:00,13:05,WORLD,EFG"])) #	None
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) #	HELLO
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) #	FOO
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # WORLD