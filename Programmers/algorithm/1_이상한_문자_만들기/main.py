# goal: 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

def solution(s):
    words_list = s.split(" ")
    answer = []

    for word in words_list:
        new_word = ""
        for index, char in enumerate(word):
            new_word += char.upper() if index % 2 == 0 else char.lower()
        answer.append(new_word)
    return " ".join(answer)