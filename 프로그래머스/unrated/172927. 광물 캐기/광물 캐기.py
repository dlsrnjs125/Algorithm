from collections import deque

def solution(picks, minerals):
    answer = 1250
    q = deque([(0,minerals,picks)]) # (피로도,남은 광물, 남은 곡괭이)
    m_val = {"diamond":2,"iron":1,"stone":0}

    while q:
        ftg,mnr,rm_picks = q.popleft()
        now_mnr,mnr = mnr[:5],mnr[5:] # 5개 기준으로 체크할 광물, 나머지 광물 나누기

        if not now_mnr or sum(rm_picks)==0: # 체크할 광물이 없거나 곡괭이를 다 썼다면
            answer = min(ftg,answer) # 저장된 피로도와 현재 피로도 중 최소를 저장
        else:
            for idx,pick in enumerate(rm_picks):
                pickax = 2-idx
                if pick != 0:
                    rm_picks[idx]-=1
                    q.append((ftg+sum(5**(max(0,m_val[m]-pickax)) for m in now_mnr),mnr,[p for p in rm_picks]))
                    rm_picks[idx]+=1
    
    
    return answer