import datetime

def solution(a, b):
    answer = ''

    # convert date from format '2016-a-b' to 'Monday', 'Tuesday' ...
    answer = datetime.datetime.strptime('2016-{}-{}'.format(a,b), '%Y-%m-%d').strftime('%A')

    # shorten to string of length 3
    answer = answer[:3].upper()

    return answer

if __name__ == "__main__":
    print(solution(5, 24)) #TUE