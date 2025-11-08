# 텍스트 전처리를 위한 내장 모듈 (re)
import re

class TextCleaner:
    # 특수문자 제거 메서드 생성
    def remove_special(self, text):
        # r은 정규표현식
        # ^는 not 부정을 의미 
        # a-zA-Z: 소문자 a부터 z, 대문자 A부터 Z
        # \s는 문자열 
        return re.sub(r'[^a-zA-Z\s]', "", text)
    
    # 소문자 변경 메서드 생성 
    def to_lower(self, text):
        return text.lower()
    
    # 위의 특수문자 제거와 소문자 변경 작업을 모두 모으는 메서드 생성
    # ["Hello!!!", "Machine-Learning??", "Python123"]
    def  clean_corpus(self, text):
        result = []

        for t in text:
            # 먼저, 특수문자 제거 작업
            t1 = self.remove_special(t)
            # 소문자 제거 작업
            t2 = self.to_lower(t1)
            # result 리스트에 추가 
            result.append(t2)

        return result



