def solution(participant, completion):
    participant_count = {}

    for name in participant:
        if name not in participant_count:
            participant_count[name] = 1
        else:
            participant_count[name] += 1

    for name in completion:
        participant_count[name] -= 1

    for (name, count) in participant_count:
        if count > 0:
            answer = name
            break

    return answer
