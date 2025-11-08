# 평균 계산 함수 생성 
# [[12, 25, 37], [15, 27, 39], [16, 30, 45]]
# 첫번째열 평균값[14.3, 27.3, 40.3]
def calculate_mean(data):
    means = [sum(col) / len(col) for col in zip(*data)]
    return means

# 분산 계산 함수 생성 
def calculate_variance(data):
    means = calculate_mean(data)
    variances = []

    # [12,15,16], [25,27,30], [37,39,45]
    for i, value in enumerate(zip(*data)): # 0, [12, 15, 16] 첫번째 결과값
        # var = sum(((12 - means[0]) ** 2) + ((15 - means[0]) ** 2) + ((16 - means[0]) ** 2) / 3) 
        var = sum((x - means[i]) ** 2 for x in value) / len(value)
        variances.append(var)

    return variances

# 함수들을 호출하여 딕셔너리로 전달하는 함수 생성
# summary()함수가 이 파일의 대장 
def  summary(data): 
    return {
        "mean": calculate_mean(data),
        "variance": calculate_variance(data)
    }