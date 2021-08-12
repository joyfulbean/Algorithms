import collections
from collections import Counter
from collections import OrderedDict

def solution(genres, plays):
    
    ## 각 장르별 플레이 횟수대로 내림차순 정렬
    genre_dict = collections.defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_dict[genre] += play
    ordered_genre = OrderedDict(sorted(genre_dict.items(), key=lambda t:t[1], reverse = True))

    ## 장르별 (플레이 횟수, 인덱스) 로 넣어준다.
    each_genre = collections.defaultdict(list)
    i = 0
    for genre, play in zip(genres, plays):
        each_genre[genre].append((play, i))
        i += 1
    
    # 내림차순 정렬 한대로 뽑아와서, 그 장르의 플레이 횟수 별로 내림차순 정렬을 하고, 최상위 2의 인덱스만 추가
    answer = []
    for genre in ordered_genre:
        print(genre)
        each_genre[genre].sort(key = lambda x:x[0], reverse=True)
        answer.append(each_genre[genre][0][1])
        if len(each_genre[genre]) > 1:
            answer.append(each_genre[genre][1][1])
    print(answer)

    return answer

