# goal: 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 1 이상인 문자열입니다.
# s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
# 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

# pseudocode
#   split s into array of string
#   for each string,
#   turn to lowercase letters
#   find the location of first letter in each string and convert that to uppercase letter
#   join all letters in the end

def solution(s):
    #   split s into array of string
    s = s.split(" ")

    #   for each word,
    for i, word in enumerate(s):
        #   turn to lowercase letters
        #   find the location of first letter in each string and convert that to uppercase letter
        s[i] = word.lower()
        if len(s[i]) > 0 and  s[i][0].isalpha():
            s[i] = capitalize_first_letter(s[i])

    #   join all letters in the end
    answer = " ".join(s)
    return answer

def capitalize_first_letter(word):
    word = [x for x in word]
    word[0] = word[0].upper()
    return "".join(word)


if __name__ == "__main__":
    print(solution("3people unFollowed me")) #3people Unfollowed Me
    print(solution("for the last week")) # For The Last Week
    print(solution("for  the last week")) # For  The Last Week
    print(solution("    ")) #