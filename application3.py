from flask import Flask, request, jsonify
import pickle
import sys
from datetime import date, timedelta,datetime
application = Flask(__name__)

rinuxtimenow = datetime.now() #리눅스 현재 시각
krtimenow = rinuxtimenow+timedelta(hours=9) # kr현재시각
tomorrow = rinuxtimenow+timedelta(days=1,hours=9) #kr 24시간 후
if(16 <= krtimenow.hour and krtimenow.hour<= 23):
    set_d = tomorrow.date()
elif (0 <= krtimenow.hour and krtimenow.hour< 16):
    set_d = krtimenow.date()
set_d = set_d.isoformat()
set_d = set_d.replace('-','')[2:]
set_d


#---------------------------------------------------------------------------------
#A파트 저장된 데이터 불러오기

# with open('daily_news.pickle','rb') as f:
#     daily_news = pickle.load(f)
import pickle5 as pickle2
with open('daily_news.pickle','rb') as f:
    daily_news = pickle2.load(f)

# with open('df_sector_A.pickle', 'rb') as f:
#     df_sector = pickle2.load(f)

df_sector = {
    'Food':{
        '097950':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '271560':['관리 모멘텀 안타',
   '매출 젤리 오리온',
   '오리온 마이 구미',
   'https://finance.naver.com/item/news_read.naver?article_id=0004085540&office_id=011&code=271560&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0002026235&office_id=016&code=271560&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0004780723&office_id=008&code=271560&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0005129852&office_id=277&code=271560&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0005287215&office_id=018&code=271560&page=1&sm=title_entity_id.basic'],
        '000080':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '004370':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '005300':['롯데 칠성 편입',
   '롯데 칠성 주가',
   '롯데 칠성 탄산음료',
   'https://finance.naver.com/item/news_read.naver?article_id=0000831697&office_id=366&code=005300&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0005282747&office_id=018&code=005300&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0000076453&office_id=024&code=005300&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0000831430&office_id=366&code=005300&page=1&sm=title_entity_id.basic',
   'https://finance.naver.com/item/news_read.naver?article_id=0004876548&office_id=014&code=005300&page=1&sm=title_entity_id.basic']
    },
    'Clothing' : {
        '093050':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '020000':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '105630':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '001070':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Chemical' : {
        '051910':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '096770':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '010950':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '051900':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '090430':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Medicine' : {
        '207940':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '068270':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '000100':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '128940':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Non_Metal' : {
        '003670':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '003410':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '010780':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Metal': {
        '005490':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '010130':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '004020':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '016380':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '001230':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Machine' : {
        '034020':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '018880':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '241560':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '112610':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Electronic' : {
        '005930':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '000660':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '006400':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '066570':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Construction' : {
        '000720':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '006360':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '047040':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '051600':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Transport': {
        '011200':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '003490':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '086280':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '180640':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '028670':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Distribution' : {
        '028260':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '023530':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '282330':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '139480':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '004170':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Power': {
        '015760':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '036460':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '017390':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Tele' : {
        '017670':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '030200':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '032640':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Finance': {
        '003550':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '000810':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '006800':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Brokerage' : {
        '005940':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '016360':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '008560':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '039490':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Insurer': {
        '032830':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '005830':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '000060':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '001450':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Service': {
        '035420':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '035720':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '018260':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '036570':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    },
    'Manufacturer': {
        '005380':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '000270':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '012330':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '033780':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '009150':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
    }
}


#-----------------------------------------------------------------------------------------
#일일 뉴스 이미지 경로 최신화(주소 최신화)
with open('daily_news_image_url_re.pickle', 'rb') as f:
    daily_news_image_url_re = pickle.load(f)

#-----------------------------------------------------------------------------------------

# 일일 뉴스 - 전체

@application.route("/daily_news_all", methods=["POST"])
def daily_news_all():

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "일일뉴스"
              },
              "items": [
                {
                  "title": "전체뉴스분석",
                  "description": "분석확인하기",
                  "imageUrl": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA3MjlfMjg4%2FMDAxNjU5MTAyMDEwOTU1.yC5GUnA29dMBrYl90MWlx10dvGcdDC31gZKUPqmhaIUg.2y-RQr7G3Mrf7_91EnZtc79sC_LnKan7HmgSILD4Q-gg.PNG.azumataiko%2F%25BD%25BA%25C5%25A9%25B8%25B0%25BC%25A6_2022-07-29_%25BF%25C0%25C8%25C4_10.40.01.png&type=sc960_832",
                  "action": "message",
                  "messageText": "전체뉴스분석",
                },
                  {
                  "title": "전체뉴스키워드",
                  "description": "키워드확인하기",
                  "imageUrl": "https://t1.daumcdn.net/cfile/tistory/996C5E455C7222192F",
                  "action": "message",
                  "messageText": "전체뉴스키워드",
                },
                  {
                  "title": "긍정뉴스",
                  "imageUrl": "http://www.supercoloring.com/sites/default/files/styles/coloring_medium/public/cif/2022/01/1-grinning-face-emoji-coloring-page.png",
                  "description": "긍정뉴스확인하기",
                  "action": "message",
                  "messageText": "긍정뉴스",
                },
                  {
                  "title": "부정뉴스",
                  "description": "부정뉴스확인하기",
                  "imageUrl": "https://www.supercoloring.com/sites/default/files/styles/coloring_medium/public/cif/2022/01/39-neutral-face-emoji-coloring-page.png",
                  "action": "message",
                  "messageText": "부정뉴스",
                },
              ],
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 전체 뉴스 - 이미지 출력

@application.route("/daily_news_all_image", methods=["POST"])
def daily_news_all_image():
    

    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "감성분석 파이그래프",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[0]
              },
            },
              {
              "title": "감성분석 막대그래프",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[1]
              },
            },
              {
              "title": "워드클라우드",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[2]
              },
            },
              {
              "title": "온도계",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[3]
              }
            }
          ]
        }
      }
    ]
  }
}

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 전체 뉴스 - 키워드 출력

all_keyword = daily_news['all']

@application.route("/daily_news_all_keyword", methods=["POST"])
def daily_news_all_keyword():
    

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "금일 전체 뉴스의 키워드는 "+all_keyword[0]+", "+all_keyword[1]+", "+all_keyword[2]+"입니다."
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 일일 뉴스 - 긍정

@application.route("/daily_news_positive", methods=["POST"])
def daily_news_positive():

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "긍정뉴스"
              },
              "items": [
                {
                  "title": "긍정뉴스분석",
                  "description": "분석확인하기",
                  "imageUrl": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA3MjlfMjg4%2FMDAxNjU5MTAyMDEwOTU1.yC5GUnA29dMBrYl90MWlx10dvGcdDC31gZKUPqmhaIUg.2y-RQr7G3Mrf7_91EnZtc79sC_LnKan7HmgSILD4Q-gg.PNG.azumataiko%2F%25BD%25BA%25C5%25A9%25B8%25B0%25BC%25A6_2022-07-29_%25BF%25C0%25C8%25C4_10.40.01.png&type=sc960_832",
                  "action": "message",
                  "messageText": "긍정뉴스분석",
                },
                  {
                  "title": "긍정뉴스키워드",
                  "description": "키워드확인하기",
                  "imageUrl": "https://t1.daumcdn.net/cfile/tistory/996C5E455C7222192F",
                  "action": "message",
                  "messageText": "긍정뉴스키워드",
                },
                  {
                  "title": "긍정뉴스링크",
                  "description": "링크확인하기",
                  "imageUrl": "https://cdn.logosian.com/news/photo/202112/3511_6504_4016.jpg",
                  "action": "message",
                  "messageText": "긍정뉴스링크",
                },
              ],
             "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : "일일뉴스",
                }
              ]   
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 긍정 뉴스 - 이미지 출력

@application.route("/daily_news_positive_image", methods=["POST"])
def daily_news_positive_image():
    

    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "감성분석 파이그래프",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[4]
              },
            },
              {
              "title": "감성분석 막대그래프",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[5]
              },
            },
              {
              "title": "워드클라우드",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[6]
              },
            },
          ]
        }
      }
    ]
  }
}

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 긍정 뉴스 - 키워드 출력

positive_keyword = daily_news['positive']

@application.route("/daily_news_positive_keyword", methods=["POST"])
def daily_news_positive_keyword():
    

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "금일 긍정 뉴스의 키워드는 "+positive_keyword[0]+", "+positive_keyword[1]+", "+positive_keyword[2]+"입니다."
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 긍정 뉴스 - 링크 출력

positive_link = daily_news['positive']

@application.route("/daily_news_positive_link", methods=["POST"])
def daily_news_positive_link():

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "긍정뉴스링크"
              },
              "items": [
                {
                  "title": "긍정뉴스1",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": positive_link[3]
                  }
                },
                  {
                  "title": "긍정뉴스2",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": positive_link[4]
                  }
                },
                  {
                  "title": "긍정뉴스3",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": positive_link[5]
                  }
                },
                  {
                  "title": "긍정뉴스4",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": positive_link[6]
                  }
                },
                  {
                  "title": "긍정뉴스5",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": positive_link[7]
                  }
                },
              ],
                "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : "긍정뉴스",
                }
              ]
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 일일 뉴스 - 부정

@application.route("/daily_news_negative", methods=["POST"])
def daily_news_negative():

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "부정뉴스"
              },
              "items": [
                {
                  "title": "부정뉴스분석",
                  "description": "분석확인하기",
                  "imageUrl": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA3MjlfMjg4%2FMDAxNjU5MTAyMDEwOTU1.yC5GUnA29dMBrYl90MWlx10dvGcdDC31gZKUPqmhaIUg.2y-RQr7G3Mrf7_91EnZtc79sC_LnKan7HmgSILD4Q-gg.PNG.azumataiko%2F%25BD%25BA%25C5%25A9%25B8%25B0%25BC%25A6_2022-07-29_%25BF%25C0%25C8%25C4_10.40.01.png&type=sc960_832",
                  "action": "message",
                  "messageText": "부정뉴스분석",
                },
                  {
                  "title": "부정뉴스키워드",
                  "description": "키워드확인하기",
                  "imageUrl": "https://t1.daumcdn.net/cfile/tistory/996C5E455C7222192F",
                  "action": "message",
                  "messageText": "부정뉴스키워드",
                },
                  {
                  "title": "부정뉴스링크",
                  "description": "링크확인하기",
                  "imageUrl": "https://cdn.logosian.com/news/photo/202112/3511_6504_4016.jpg",
                  "action": "message",
                  "messageText": "부정뉴스링크",
                },
              ],
                "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : "일일뉴스",
                }
              ]   
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)



#-----------------------------------------------------------------------------------------
# 부정 뉴스 - 이미지 출력

@application.route("/daily_news_negative_image", methods=["POST"])
def daily_news_negative_image():
    

    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "감성분석 파이그래프",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[7]
              },
            },
              {
              "title": "감성분석 막대그래프",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[8]
              },
            },
              {
              "title": "워드클라우드",
              "thumbnail": {
                "imageUrl": daily_news_image_url_re[9]
              },
            },
          ]
        }
      }
    ]
  }
}

    # 답변 전송
    return jsonify(response)


#-----------------------------------------------------------------------------------------
# 부정 뉴스 - 키워드 출력

negative_keyword = daily_news['negative']

@application.route("/daily_news_negative_keyword", methods=["POST"])
def daily_news_negative_keyword():
    

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "금일 부정 뉴스의 키워드는 "+negative_keyword[0]+", "+negative_keyword[1]+", "+negative_keyword[2]+"입니다."
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)


#-----------------------------------------------------------------------------------------
# 부정 뉴스 - 링크 출력

negative_link = daily_news['negative']

@application.route("/daily_news_negative_link", methods=["POST"])
def daily_news_negative_link():

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "부정뉴스링크"
              },
              "items": [
                {
                  "title": "부정뉴스1",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": negative_link[3]
                  }
                },
                  {
                  "title": "부정뉴스2",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": negative_link[4]
                  }
                },
                  {
                  "title": "부정뉴스3",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": negative_link[5]
                  }
                },
                  {
                  "title": "부정뉴스4",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": negative_link[6]
                  }
                },
                  {
                  "title": "부정뉴스5",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": negative_link[7]
                  }
                },
              ],
                "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : "부정뉴스",
                }
              ]
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)

#-----------------------------------------------------------------------------------------
# 업종별 리스트 출력 (Carousel)

@application.route("/sector", methods=["POST"])
def sector():
    

    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "음식료품, 섬유의복",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Clothing-Food.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "음식료품",
                  "messageText": '음식료품'
                },
                {
                  "action":  "message",
                  "label": "섬유의복",
                  "messageText": '섬유의복'
                }
              ]
            },
            {
              "title": "화학, 의약품",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Medicine-Chemical.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "화학",
                  "messageText": '화학'
                },
                {
                  "action":  "message",
                  "label": "의약품",
                  "messageText": '의약품'
                }
              ]
            },
              {
              "title": "비금속광물, 철강금속",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Metal-NonMetal.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "비금속광물",
                  "messageText": '비금속광물'
                },
                {
                  "action":  "message",
                  "label": "철강금속",
                  "messageText": '철강금속'
                }
              ]
            },
              {
              "title": "기계, 전기전자",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Electronic-Machine.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "기계",
                  "messageText": '기계'
                },
                {
                  "action":  "message",
                  "label": "전기전자",
                  "messageText": '전기전자'
                }
              ]
            },
              {
              "title": "건설업, 운수창고",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Transport-Construction.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "건설업",
                  "messageText": '건설업'
                },
                {
                  "action":  "message",
                  "label": "운수창고",
                  "messageText": '운수창고'
                }
              ]
            },
              {
              "title": "유통업, 전기가스업",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Power-Distribution.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "유통업",
                  "messageText": '유통업'
                },
                {
                  "action":  "message",
                  "label": "전기가스업",
                  "messageText": '전기가스업'
                }
              ]
            },
              {
              "title": "통신업, 금융업",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Finance-Tele.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "통신업",
                  "messageText": '통신업'
                },
                {
                  "action":  "message",
                  "label": "금융업",
                  "messageText":'금융업'
                }
              ]
            },
              {
              "title": "증권, 보험",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Insure-Brokerage.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "증권",
                  "messageText": '증권'
                },
                {
                  "action":  "message",
                  "label": "보험",
                  "messageText": '보험'
                }
              ]
            },
              {
              "title": "서비스업, 제조업",
              "description": set_d+"일자 업종 내 종목 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Manufacturer-Service.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "서비스업",
                  "messageText": '서비스업'
                },
                {
                  "action":  "message",
                  "label": "제조업",
                  "messageText": '제조업'
                }
              ]
            }
          ]
        }
      }
    ]
  }
}

    # 답변 전송
    return jsonify(response)


#---------------------------------------------------------------------------------------------------
#업종별 종목 리스트 출력(ListCard)



sector_l = {
    '음식료품' : ['CJ제일제당','오리온', '하이트진로', '농심', '롯데칠성'],
    '섬유의복' : ['LF', '한섬', '한세실업', '대한방직'],
    '화학' : ['LG화학', 'SK이노베이션', 'S-Oil', 'LG생활건강', '아모레퍼시픽'],
    '의약품' :  ['삼성바이오로직스', '셀트리온', '유한양행', '한미약품'],
    '비금속광물' : ['포스코케미칼', '쌍용C&E', '아이에스동서'],
    '철강금속' : ['POSCO홀딩스', '고려아연', '현대제철', 'KG스틸', '동국제강'],
    '기계' : ['두산에너빌리티', '한온시스템', '두산밥캣', '씨에스윈드'],
    '전기전자': ['삼성전자', 'SK하이닉스', '삼성SDI', 'LG전자'],
    '건설업' : ['현대건설', 'GS건설', '대우건설', '한전KPS'],
    '운수창고' : ['HMM', '대한항공', '현대글로비스', '한진칼', '팬오션'],
    '유통업' : ['삼성물산', '롯데쇼핑', 'BGF리테일', '이마트', '신세계'],
    '전기가스업' : ['한국전력', '한국가스공사', '서울가스'],
    '통신업' : ['SK테레콤', 'KT', 'LG유플러스'],
    '금융업' :  ['LG' , '삼성화재', '미래에셋증권'],
    '증권' : ['NH투자증권' ,'삼성증권', '메리츠증권', '키움증권'],
    '보험' : ['삼성생명', 'DB손해보험', '메리츠화재', '현대해상'],
    '서비스업' : ['Naver', '카카오', '삼성에스디에스', '엔씨소프트'],
    '제조업' :  ['현대차', '기아', '현대모비스', 'KT&G', '삼성전기']
}


def sector_l_response(answer,n):
    if n==1:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://img.danawa.com/prod_img/500000/284/976/img/8976284_1.jpg?shrink=330:330&_v=20190802153645",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
        ]
    elif n==2:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://img.danawa.com/prod_img/500000/164/976/img/8976164_1.jpg?shrink=330:330&_v=20190802153555",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://img.danawa.com/prod_img/500000/452/976/img/8976452_1.jpg?shrink=330:330&_v=20190802154103",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
        ]
    elif n==3:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FO16783343728.jpg%3Fut%3D20220324163643",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/2021/03/08/15/3/3c275dcf-458d-4af1-8bc2-45ed7ea70219.jpg",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
            {
              "title": sector_l[answer][2],
              "imageUrl": "https://img.danawa.com/prod_img/500000/044/976/img/8976044_1.jpg?shrink=330:330&_v=20190802153539",
              "action": "message",
              "messageText": sector_l[answer][2],
              },
        ]
    elif n==4:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/product/3181252337/B.jpg?479000000",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://img.danawa.com/prod_img/500000/284/976/img/8976284_1.jpg?shrink=330:330&_v=20190802153645",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
            {
              "title": sector_l[answer][2],
              "imageUrl": "http://image.kyobobook.co.kr/newimages/giftshop_new/goods/400/1730/hot1539673071039.jpg",
              "action": "message",
              "messageText": sector_l[answer][2],
              },
            {
              "title": sector_l[answer][3],
              "imageUrl": "http://mstatic1.e-himart.co.kr/contents/goods/00/15/59/76/87/0015597687__MW64027_1944709__M_640_640.jpg",
              "action": "message",
              "messageText": sector_l[answer][3],
              },
        ]
    elif n==5:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FO16783343728.jpg%3Fut%3D20220324163643",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/2021/03/08/15/3/3c275dcf-458d-4af1-8bc2-45ed7ea70219.jpg",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
            {
              "title": sector_l[answer][2],
              "imageUrl": "https://img.danawa.com/prod_img/500000/044/976/img/8976044_1.jpg?shrink=330:330&_v=20190802153539",
              "action": "message",
              "messageText": sector_l[answer][2],
              },
            {
              "title": sector_l[answer][3],
              "imageUrl": "https://img.danawa.com/prod_img/500000/164/976/img/8976164_1.jpg?shrink=330:330&_v=20190802153555",
              "action": "message",
              "messageText": sector_l[answer][3],
              },
            {
              "title": sector_l[answer][4],
              "imageUrl": "https://img.danawa.com/prod_img/500000/452/976/img/8976452_1.jpg?shrink=330:330&_v=20190802154103",
              "action": "message",
              "messageText": sector_l[answer][4],
              },
        ]
    return res
        

@application.route("/stock", methods=["POST"])
def stock():
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['sector_entity']['value']   # json파일 읽기
    n = len(sector_l[answer])
    res = sector_l_response(answer,n)
    
    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": answer
          },
          "items": res,
            "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : "업종별",
                }
              ]
        }
      }
    ]
  }
}

    return jsonify(response)




#---------------------------------------------------------------------------------------------------
#종목 리스트 출력

with open('back_dic.pickle','rb') as f:
    back_dic = pickle.load(f)

@application.route("/stock_l", methods=["POST"])
def stock_l():
    
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['stock_l_entity']['value']   # json파일 읽기

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": answer
              },
              "items": [
                {
                  "title": answer+ " 시세 방향 추이",
              	  "description": set_d+"일자 시세 확인",
                  "imageUrl": "https://img.lovepik.com/photo/50030/2947.jpg_wh860.jpg",
                  "action": "message",
                  "messageText": answer+"시세",
                },
                  {
                  "title": answer+" 전체분석",
                  "imageUrl": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA3MjlfMjg4%2FMDAxNjU5MTAyMDEwOTU1.yC5GUnA29dMBrYl90MWlx10dvGcdDC31gZKUPqmhaIUg.2y-RQr7G3Mrf7_91EnZtc79sC_LnKan7HmgSILD4Q-gg.PNG.azumataiko%2F%25BD%25BA%25C5%25A9%25B8%25B0%25BC%25A6_2022-07-29_%25BF%25C0%25C8%25C4_10.40.01.png&type=sc960_832",
                  "description": "분석확인하기",
                  "action": "message",
                  "messageText": answer+"분석",
                },
                  {
                  "title": answer+" 뉴스키워드",
                  "description": "키워드확인하기",
                  "imageUrl": "https://t1.daumcdn.net/cfile/tistory/996C5E455C7222192F",
                  "action": "message",
                  "messageText": answer+"키워드",
                },
                  {
                  "title": answer+" 뉴스링크",
                  "description": "링크확인하기",
                  "imageUrl": "https://cdn.logosian.com/news/photo/202112/3511_6504_4016.jpg",
                  "action": "message",
                  "messageText": answer+"뉴스링크",
                },
              ],
                "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : back_dic[answer],
                }
              ]
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)



#---------------------------------------------------------------------------------------------------
#종목 예상 값 출력
with open('pred_dic.pickle','rb') as f:
    pred_dic = pickle.load(f)
    
with open('certificated_stock_dic.pickle','rb') as f:
    certificated_stock_dic = pickle.load(f)
    
with open('sector.pickle', 'rb') as f:
    sector1 = pickle.load(f)
    
sector2 = {
    '음식료품' : ['CJ제일제당','오리온', '하이트진로', '농심', '롯데칠성'],
    '섬유의복' : ['LF', '한섬', '한세실업', '대한방직'],
    '화학' : ['LG화학', 'SK이노베이션', 'S-Oil', 'LG생활건강', '아모레퍼시픽'],
    '의약품' :  ['삼성바이오로직스', '셀트리온', '유한양행', '한미약품'],
    '비금속광물' : ['포스코케미칼', '쌍용C&E', '아이에스동서'],
    '철강금속' : ['POSCO홀딩스', '고려아연', '현대제철', 'KG스틸', '동국제강'],
    '기계' : ['두산에너빌리티', '한온시스템', '두산밥캣', '씨에스윈드'],
    '전기전자': ['삼성전자', 'SK하이닉스', '삼성SDI', 'LG전자'],
    '건설업' : ['현대건설', 'GS건설', '대우건설', '한전KPS'],
    '운수창고' : ['HMM', '대한항공', '현대글로비스', '한진칼', '팬오션'],
    '유통업' : ['삼성물산', '롯데쇼핑', 'BGF리테일', '이마트', '신세계'],
    '전기가스업' : ['한국전력', '한국가스공사', '서울가스'],
    '통신업' : ['SK테레콤', 'KT', 'LG유플러스'],
    '금융업' :  ['LG' , '삼성화재', '미래에셋증권'],
    '증권' : ['NH투자증권' ,'삼성증권', '메리츠증권', '키움증권'],
    '보험' : ['삼성생명', 'DB손해보험', '메리츠화재', '현대해상'],
    '서비스업' : ['Naver', '카카오', '삼성에스디에스', '엔씨소프트'],
    '제조업' :  ['현대차', '기아', '현대모비스', 'KT&G', '삼성전기']
}

sector_code = []
for sectorname, stock_list in sector1.items():
    for stock in stock_list:
        sector_code.append(sectorname+stock)
        
sector_name =[]
for sectorname, stock_list in sector2.items():
    for stock in stock_list:
        sector_name.append(stock)
        
stock_dic={}
for i in range(len(sector_code)):
    stock_dic[sector_code[i]]=sector_name[i]
    
pred_dic_select ={}
for i, j in pred_dic.items():
    for k in j: 
        pred_dic_select[i+k] = pred_dic[i][k]
        
pred_dic_select_str = {}
for i, j in pred_dic_select.items():
    정확도 = float(j[0][11:])
    상향 = float(j[1][9:])
    하향 = float(j[2][9:])
    횡보 = float(j[3][9:])
    최대 = max(상향,하향,횡보)
    if 최대 == 상향:
        pred_dic_select_str[i] = f'상향이 예상됩니다. 정확도는 {정확도}%입니다.'
    elif 최대 == 하향:
        pred_dic_select_str[i] = f'하향이 예상됩니다. 정확도는 {정확도}%입니다.'
    elif 최대 == 횡보:
        pred_dic_select_str[i] = f'횡보가 예상됩니다. 정확도는 {정확도}%입니다.'
    
result_dic = {}
for i,j in stock_dic.items():
    if i not in list(pred_dic_select_str.keys()):
        result_dic[i]='해당 종목은 정확도 항샹을 위한 성능 개선중에 있습니다.'
    else:
        result_dic[i]=pred_dic_select_str[i]    
        
result_l = {}
for i,j in result_dic.items():
    result_l[stock_dic[i]]=j
    
result_l_price = {}
for i,j in result_l.items():
    result_l_price[i+'시세'] = j
    
@application.route("/stock_price", methods=["POST"])
def stock_price():
    
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['stock_price_entity']['value']   # json파일 읽기
    n = len(answer) - 2

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer[:n] + '의 ' + set_d + '일자 ' + result_l_price[answer]
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)


#-----------------------------------------------------------------------------------------
#종목 이미지 경로 최신화(주소 최신화)
with open('df_sector_image_url.pickle', 'rb') as f:
    df_sector_image_url = pickle.load(f)


#-----------------------------------------------------------------------------------------
#종목 분석 출력

@application.route("/stock_image", methods=["POST"])
def stock_image():
    
    
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['stock_image_entity']['value']   # json파일 읽기
    n = len(answer) - 2
    
    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "감성분석 파이그래프",
              "thumbnail": {
                "imageUrl": df_sector_image_url[answer][0]
              },
            },
              {
              "title": "감성분석 막대그래프",
              "thumbnail": {
                "imageUrl": df_sector_image_url[answer][1]
              },
            },
              {
              "title": "워드클라우드",
              "thumbnail": {
                "imageUrl": df_sector_image_url[answer][2]
              },
            },
              {
              "title": "온도계",
              "thumbnail": {
                "imageUrl": df_sector_image_url[answer][3]
              }
            }
          ]
        }
      }
    ]
  }
}

    # 답변 전송
    return jsonify(response)



#-----------------------------------------------------------------------------------------
#종목 키워드 출력
def stock_keyword_dic():
    sector2 = {
    '음식료품' : ['CJ제일제당','오리온', '하이트진로', '농심', '롯데칠성'],
    '섬유의복' : ['LF', '한섬', '한세실업', '대한방직'],
    '화학' : ['LG화학', 'SK이노베이션', 'S-Oil', 'LG생활건강', '아모레퍼시픽'],
    '의약품' :  ['삼성바이오로직스', '셀트리온', '유한양행', '한미약품'],
    '비금속광물' : ['포스코케미칼', '쌍용C&E', '아이에스동서'],
    '철강금속' : ['POSCO홀딩스', '고려아연', '현대제철', 'KG스틸', '동국제강'],
    '기계' : ['두산에너빌리티', '한온시스템', '두산밥캣', '씨에스윈드'],
    '전기전자': ['삼성전자', 'SK하이닉스', '삼성SDI', 'LG전자'],
    '건설업' : ['현대건설', 'GS건설', '대우건설', '한전KPS'],
    '운수창고' : ['HMM', '대한항공', '현대글로비스', '한진칼', '팬오션'],
    '유통업' : ['삼성물산', '롯데쇼핑', 'BGF리테일', '이마트', '신세계'],
    '전기가스업' : ['한국전력', '한국가스공사', '서울가스'],
    '통신업' : ['SK테레콤', 'KT', 'LG유플러스'],
    '금융업' :  ['LG' , '삼성화재', '미래에셋증권'],
    '증권' : ['NH투자증권' ,'삼성증권', '메리츠증권', '키움증권'],
    '보험' : ['삼성생명', 'DB손해보험', '메리츠화재', '현대해상'],
    '서비스업' : ['Naver', '카카오', '삼성에스디에스', '엔씨소프트'],
    '제조업' :  ['현대차', '기아', '현대모비스', 'KT&G', '삼성전기']
    }
    stock_l = []
    for i in sector2.keys():
        for j in sector2[i]:
            stock_l.append(j)
            
    stock_l_add = []
    for i in stock_l:
        stock_l_add.append(i+'키워드')
        
    stock_l_add_keyword = []
    for i,j in df_sector.items():
        for k,r in j.items():
            stock_l_add_keyword.append(r[:3])
        
    stock_keyword = {}
    for i in range(len(stock_l_add)):
        stock_keyword[stock_l_add[i]]=stock_l_add_keyword[i]
    
    return stock_keyword


@application.route("/stock_keyword", methods=["POST"])
def stock_keyword():
    
    result_l_keyword = stock_keyword_dic()
    
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['stock_keyword_entity']['value']   # json파일 읽기
    n = len(answer) - 3

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : answer[:n]+ " 뉴스의 키워드는 "+ result_l_keyword[answer][0]+", "+ result_l_keyword[answer][1]+", "+ result_l_keyword[answer][2]+"입니다."
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)






#-----------------------------------------------------------------------------------------
#종목 뉴스링크 출력

def stock_link_dic():
    sector2 = {
    '음식료품' : ['CJ제일제당','오리온', '하이트진로', '농심', '롯데칠성'],
    '섬유의복' : ['LF', '한섬', '한세실업', '대한방직'],
    '화학' : ['LG화학', 'SK이노베이션', 'S-Oil', 'LG생활건강', '아모레퍼시픽'],
    '의약품' :  ['삼성바이오로직스', '셀트리온', '유한양행', '한미약품'],
    '비금속광물' : ['포스코케미칼', '쌍용C&E', '아이에스동서'],
    '철강금속' : ['POSCO홀딩스', '고려아연', '현대제철', 'KG스틸', '동국제강'],
    '기계' : ['두산에너빌리티', '한온시스템', '두산밥캣', '씨에스윈드'],
    '전기전자': ['삼성전자', 'SK하이닉스', '삼성SDI', 'LG전자'],
    '건설업' : ['현대건설', 'GS건설', '대우건설', '한전KPS'],
    '운수창고' : ['HMM', '대한항공', '현대글로비스', '한진칼', '팬오션'],
    '유통업' : ['삼성물산', '롯데쇼핑', 'BGF리테일', '이마트', '신세계'],
    '전기가스업' : ['한국전력', '한국가스공사', '서울가스'],
    '통신업' : ['SK테레콤', 'KT', 'LG유플러스'],
    '금융업' :  ['LG' , '삼성화재', '미래에셋증권'],
    '증권' : ['NH투자증권' ,'삼성증권', '메리츠증권', '키움증권'],
    '보험' : ['삼성생명', 'DB손해보험', '메리츠화재', '현대해상'],
    '서비스업' : ['Naver', '카카오', '삼성에스디에스', '엔씨소프트'],
    '제조업' :  ['현대차', '기아', '현대모비스', 'KT&G', '삼성전기']
    }
    stock_l = []
    for i in sector2.keys():
        for j in sector2[i]:
            stock_l.append(j)
            
    stock_l_add = []
    for i in stock_l:
        stock_l_add.append(i+'뉴스링크')
        
    stock_l_add_link = []
    for i,j in df_sector.items():
        for k,r in j.items():
            stock_l_add_link.append(r[3:])
        
    stock_link = {}
    for i in range(len(stock_l_add)):
        stock_link[stock_l_add[i]]=stock_l_add_link[i]
    
    return stock_link

@application.route("/stock_link", methods=["POST"])
def stock_link():
    
    result_l_link = stock_link_dic()
    
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['stock_link_entity']['value']   # json파일 읽기
    n = len(answer) - 4

    # 답변 텍스트 설정
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": answer[:n]+"뉴스링크"
              },
              "items": [
                {
                  "title": "뉴스1",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": result_l_link[answer][0]
                  }
                },
                  {
                  "title": "뉴스2",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": result_l_link[answer][1]
                  }
                },
                  {
                  "title": "뉴스3",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": result_l_link[answer][2]
                  }
                },
                  {
                  "title": "뉴스4",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": result_l_link[answer][3]
                  }
                },
                  {
                  "title": "뉴스5",
                  "description": "뉴스확인하기",
                  #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                  "link": {
                    "web": result_l_link[answer][4]
                  }
                },
              ],
                "buttons": [
                {
                  "label": "뒤로가기",
                  "action": "message",
                  "messageText" : answer[:n],
                }
              ]
            }
          }
        ]
      }
    }

    # 답변 전송
    return jsonify(response)



#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)