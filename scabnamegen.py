import random

def scabnamegen(live, name):
    location=random.choice(["국회의사당", "지하철", "왁싱샵", "스터디카페", "삼성프라자", "서울104번시내버스", "국어학원", "대형마트"])
    object=random.choice(["휴지", "도리토스", "마운틴듀", "냉장고", "컴퓨터", "운전대", "모자", "게임기"])
    behavior=random.choice(["훔치는", "낙서하는", "열고있는", "부수는", "해킹하는", "구독하는"])
    return live+location+object+behavior+name
