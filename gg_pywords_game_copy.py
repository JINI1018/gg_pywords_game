from pygame import mixer
import random
import time
import csv
import pandas as pd

mixer.init()
good_sound = mixer.Sound('assets/good.wav')
bad_sound = mixer.Sound('assets/bad.wav')

words = pd.read_csv("TOEIC_words.csv")

def gameRun():
    selected_day = input("진행할 day를 입력해 주세요. 예) day1~30:")
    day_words = words[words["Day"] == selected_day]
    selected_num = input("진행할 단어 개수를 입력해 주세요. 예) 1~38:")

    for index, value in enumerate(range(int(selected_num))):
        random_index = random.choice(day_words.index)
        random_row = day_words.loc[random_index, ["단어", "뜻", "외움"]]
        correct_answers = [x.strip() for x in random_row["뜻"].split(',')]
        
        print(f"문제 #{index+1}, \n 제시된 단어: {random_row['단어']}")
        input_text = input("제시된 단어의 뜻을 입력하세요:")
        user_answers = [x.strip() for x in input_text.split(',')]

        if pd.notna(random_row["외움"]):
              continue

        correct_count = 0

        for answer in user_answers:
            if answer in correct_answers:
                correct_count += 1

        point = correct_count / len(correct_answers)

        words.loc[random_index, "외움"] = point

        if point == 1:
                good_sound.play()
                time.sleep(1)
                print("모두 맞췄습니다!")
        elif 1 > point > 0:
                good_sound.play()
                time.sleep(1)
                print(f"일부만 맞았습니다. 정답은 {random_row["뜻"]}입니다.")
        else:
                bad_sound.play()
                time.sleep(1)
                print(f"틀렸습니다. 정답은 {random_row["뜻"]}입니다.")
                continue

        words.to_csv("TOEIC_words.csv", index=False, encoding="utf-8-sig")
        
    return point

gameRun()


# with open('word_game_score.csv', mode='a', newline='', encoding='utf8') as f:
#     writer = csv.writer(f)
#     writer.writerow([f'{elapsed_time:.2f}', score])