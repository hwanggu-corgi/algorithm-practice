# goal: 무지를 도와 파일명 정렬 프로그램을 구현하라.

# 입력 형식
# 입력으로 배열 files가 주어진다.

#   - files는 1000 개 이하의 파일명을 포함하는 문자열 배열이다.
#   - 각 파일명은 100 글자 이하 길이로, 영문 대소문자, 숫자, 공백(" ), 마침표(.), 빼기 부호(-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.
#   - 중복된 파일명은 없으나, 대소문자나 숫자 앞부분의 0 차이가 있는 경우는 함께 주어질 수 있다. (muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT는 함께 입력으로 주어질 수 있다.)

# Example
#   1) [img12.png, img10.png, img02.png, img1.png, IMG01.GIF, img2.JPG]
#      [img1.png, IMG01.GIF, img02.png, img2.JPG, img10.png, img12.png]

def solution(files):
    answer = []

    return answer