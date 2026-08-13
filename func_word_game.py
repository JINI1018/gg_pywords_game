import random # 단어 무작위 선택
import time #게임시작 부터 종료까지 총 걸린 시간 측정을 위해
from pygame  import mixer
mixer.init()
grom pathlib

# 클래스 정의
class WordGame:
    # 속성: words, cor_cnt, cnt
    def __init__(self):
        self.words = []
        self.cor_cnt = 0
        self.cnt = 1

    #메서드
    def wordLoad(self):
        # 파일 읽기
        path = "data/word.txt"
        words = []
        with open(path, "r", encoding="UTF8") as file:
            read_words = file.readlines()

            for word in read_words:
                # 각 단어의 공백 및 뉴라인 문자 제거
                word = word.strip()

                # 각 단어를 words 리스트에 저장
                words.append(word)

        # print(type(words))
        # print(words)
        return words

    # words = wordLoad()

    def gameRun(self) : 
        # 게임 시작 싸인 받기
        input("준비? 엔트를 입력하세요.")

        # 게임 횟수 카운트 변수
        cnt = 1
        cor_cnt = 0 # 정답 카운트
        game_time = 0
        # 게임 시작 시간
        start = time.time()
        while cnt <= 5 :
            # 문제 번호 출력
            print(f"Question #{cnt}")

            # word 하나가 랜덤하게 뽑아서 제시 : q
            random.shuffle(self.words)
            q = random.choice(self.words)
            print(q)

            a = q.strip()
            # 게이머가 입력 : answer
            answer = input()

            # 입력 워드의 양쪽 공백 삭제
            answer = answer.strip()
            if q == answer :
                # pass
                # cor_cnt 증가
                # cor_cnt += cor_cnt
                cor_cnt = cor_cnt + 1
                # 띵똥 소리 출력
                mixer.music.load('assets/good.wav') # 단어를 맞췄을 때의 소리파일 로딩
                mixer.music.play() # 소리 출력
                print()

            else:
            # 틀린 경우
                # 삐 소리 출력
                mixer.music.load('assets/bad.wav') # 단어를 맞췄을 때의 소리파일 로딩
                mixer.music.play() # 소리 출력

            cnt = cnt + 1

        end = time.time()
        # 총 걸린 시간
        et = round((end - start), 3)

        return cor_cnt, et

    # cor_cnt, et = gameRun(words)


    def scorePrint(self):

        print(f"게임종료 : 맞춘 갯수 {self.cor_cnt}, 걸린 시간 {self.et}")


    def run(self):
        # - 워드 파일을 로딩하여 words 리스트에 대입하는 기능 모듈화 : wordLoad()
        words = self.wordLoad()
        # - 워드 게임 실행하는 기능 모듈화 : gameRun()
        cor_cnt, et = self.gameRun()
        # - 게임 결과 출력 : scorePrint
        self.scorePrint()


if __name__ == "__main__":
    # 게임 객체화
    wg = WordGame()
    # 객체를 통한 게임 실행
    wg.run()
