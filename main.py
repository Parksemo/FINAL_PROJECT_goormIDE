import schedule
import time
import import_ipynb


#스케쥴 모듈이 동작시킬 코드 : 현재 시간 출력
def test_function():
    import UTDdata
    import PredictTomorrow2
    

# def test_function2():
#     import main2

#매일 특정시간에 동작
#07:00+ 9시간 = 16시
schedule.every().day.at('07:00').do(test_function)
#schedule.every().day.at('07:00').do(test_function2)


#무한 루프를 돌면서 스케쥴을 유지한다.
while True:
    schedule.run_pending()
    time.sleep(1)

