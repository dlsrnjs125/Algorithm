def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    t_year, t_month, t_day = map(int, today.split("."))
    
    for t in terms:
        alp, num = t.split()
        term_dict[alp] = int(num)
    
    for idx, pri in enumerate(privacies):
        priday, term = pri.split()
        year, month, day = map(int, priday.split('.'))
        for alp in term_dict.keys():
            if term == alp:
                month += term_dict[alp]
                while True:
                    if month > 12:
                        year += 1
                        month = month - 12
                    else:
                        break
        if t_year > year:
            answer.append(idx + 1)
        elif (year == t_year) and (t_month > month):
            answer.append(idx + 1)
        elif (year == t_year) and (t_month == month) and (t_day >= day):
            answer.append(idx + 1)
            
    return answer