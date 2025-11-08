# print(list(zip([[10, 20, 30], [20, 30, 40], [30, 40, 50]])))
# 0번자리의 최소값, 1번 자리의 최소값, 2번 자리의 최소값을 구하면 됨

class Datascaler:
    # fit() 함수에서 최소값, 최대값을 구하기 위해 
    # 최소값, 최대값 초기화 작업을 먼저 진행(변수를 선언)
    def __init__(self): 
        self.min = None  # 숫자 0을 넣어도 되고 none을 넣어도 되고. 변수를 만들어주기만 하면 됨
        self.max = None  # 0

    # 최대값, 최소값을 구하는 함수 생성
    # [[12, 25, 37], [15, 27, 39], [16, 30, 45]]
    # zip([[12, 25, 37], [15, 27, 39], [16, 30, 45]]) -> [([12,15, 16], [25, 37, 30], [37, 39, 45])]
    def fit(self, data):
        self.min = [min(col) for col in zip(*data)]  # -> [12, 25, 37]
        self.max = [max(col) for col in zip(*data)]  # -> [16, 30, 45]
    
    # min-max scaling
    def transform(self, data): 
        scaled = []

        for row in data: # [12, 25, 37], [15, 27, 39], [16, 30, 45]
            new_row = []
            for i, value in enumerate(row): # [12, 27, 37]
                new_row.append((value - self.min[i]) / (self.max[i] - self.min[i]))
                # new_row.append((12 - self.min[0]) / (self.max[0] - self.min[0]) ))
                # new_row.append((12 - 12) / (16 - 12) ))   처음 연산은 이렇게 시작
            scaled.append(new_row)

        return scaled
    
    # fit, transform 한번에 수행 
    def fit_transform(self, data):
        # 클래스 내부의 fit() 함수를 불러왔기 때문에 self를 앞에 붙여서 호출 
        self.fit(data)
        # transform() 함수를 호출한 결과를 전달함
        return self.transform(data)
    