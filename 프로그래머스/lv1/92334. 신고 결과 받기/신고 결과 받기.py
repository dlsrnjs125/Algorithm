def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {}
    id_dict = {}
    
    for i in id_list:
        report_dict[i] = 0
        id_dict[i] = []
    
    for i in set(report): # set -> 중복 제거
        i = i.split(" ")
        report_dict[i[1]] += 1
        id_dict[i[1]].append(i[0])

    for a, b in report_dict.items():
        if b >= k:
            for x in id_dict[a]:
                answer[id_list.index(x)] += 1
                    
    return answer