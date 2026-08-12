from pygame import mixer
import random
import time
import csv

mixer.init()
good_sound = mixer.Sound('assets/good.wav')
bad_sound = mixer.Sound('assets/bad.wav')

words = []
def wordLoad():
    with open("word.txt", 'r', encoding='utf8') as f:
        for line in f:
            words.append(line.strip())

wordLoad()

def gameRun():
    score = 0
    input("준비? 엔터를 입력하세요.")
    start_time = time.time()
    for index, value in enumerate(range(5)):

        word = random.choice(words)
        print(f"Question #{index+1}, \n 제시된 단어: {word}")
        input_text = input("제시된 단어를 입력하세요:")

        if input_text == word:
            score +=1
            good_sound.play()
            time.sleep(1)
            print("맞췄습니다!")
            
        else:
            bad_sound.play()
            time.sleep(1)
            print("틀렸습니다..")
            continue
    end_time = time.time()
    elapsed_time = end_time - start_time
    return score, elapsed_time

score, elapsed_time = gameRun()

def scorePrint():
    if score >= 3:
        print(f"합격했습니다.\n게임 걸린시간 : {elapsed_time:.2f}초, 맞춘 개수 : {score}개")
    else:
        print(f"불합격했습니다.\n게임 걸린시간 : {elapsed_time:.2f}초, 맞춘 개수 : {score}개")

scorePrint()

with open('word_game_score.csv', mode='a', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow([f'{elapsed_time:.2f}', score])