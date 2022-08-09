# import pickle
# with open('2022-07-26 pred_dic.pickle','rb') as f:
#     pred_dic = pickle.load(f)

# from flask import Flask, jsonify
# import sys
# import random
# application = Flask(__name__)


# @application.route("/Food", methods=["POST"])
# def random_function():
#     response = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText" : {
#                         "text": pred_dic['Food']
#                     }
#                 }
#             ]
#         } 
#     }
#     return jsonify(response)


# if __name__ == "__main__":
#     application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
    
    

# ----------------------------------------------------------------------------------------------------------------------------------------



# from flask import Flask, request, jsonify
# import pickle
# import sys


# with open('2022-07-26 pred_dic.pickle','rb') as f:
#     pred_dic = pickle.load(f)


# req ={
#     "action": {
#     "id": "123456789012",
#     "name": "spell_check",
#     "params": {
#       "spell_check_text": ""
#     },
#     "detailParams": {
#       "spell_check_text": {
#         "groupName": "",
#         "origin": "",
#         "value": pred_dic['Food']
#       }
#     },
#     "clientExtra": {}
#   }
# }
    
# application = Flask(__name__)


# @application.route("/redflavor", methods=["POST"])
# def redflavor():
    
    
    
#     answer = req["action"]["detailParams"]["spell_check_text"]["value"]	# json파일 읽기

#     # 답변 텍스트 설정
#     response = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText": {
#                         "text": answer
#                     }
#                 }
#             ]
#         }
#     }

#     # 답변 전송
#     return jsonify(response)

# if __name__ == "__main__":
#     application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
    
    
    
    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------




# from flask import Flask, request, jsonify
# import pickle
# import sys


# with open('2022-07-26 pred_dic.pickle','rb') as f:
#     pred_dic = pickle.load(f)
    
# application = Flask(__name__)


# @application.route("/redflavor", methods=["POST"])
# def redflavor():
    

#     # 답변 텍스트 설정
#     response = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "basicCard": {
#                         "title": "보물상자",
#                         "description": "보물상자 안에는 뭐가 있을까",
#                         "thumbnail": {
#                             "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
#                         },
#                         "profile": {
#                             "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
#                             "nickname": "보물상자"
#                         },
#                         "social": {
#                             "like": 1238,
#                             "comment": 8,
#                             "share": 780
#                         },
#                         "buttons": [
#                             {
#                                 "action": "message",
#                                 "label": "열어보기",
#                                 "messageText": "짜잔! 우리가 찾던 보물입니다"
#                             },
#                             {
#                                 "action":  "webLink",
#                                 "label": "구경하기",
#                                 "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
#                             }
#                         ]
#                     }
#                 }
#             ]
#         }
#     }

#     # 답변 전송
#     return jsonify(response)

# if __name__ == "__main__":
#     application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# from flask import Flask, request, jsonify
# import pickle
# import sys
# import datetime


# with open('2022-07-27 pred_dic.pickle','rb') as f:
#     pred_dic = pickle.load(f)
    
# application = Flask(__name__)


# @application.route("/redflavor", methods=["POST"])
# def redflavor():
    

#     # 답변 텍스트 설정
#     response = {
#   "version": "2.0",
#   "template": {
#     "outputs": [
#       {
#         "carousel": {
#           "type": "basicCard",
#           "items": [
#             {
#               "title": "음식료품, 섬유의복",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%9D%8C%EC%8B%9D%EB%A3%8C%ED%92%88,%EC%84%AC%EC%9C%A0%EC%9D%98%EB%B3%B5.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "음식료품",
#                   "messageText": pred_dic["Food"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "섬유의복",
#                   "messageText": pred_dic["Clothing"]
#                 }
#               ]
#             },
#             {
#               "title": "화학, 의약품",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%ED%99%94%ED%95%99,%EC%9D%98%EC%95%BD%ED%92%88.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "화학",
#                   "messageText": pred_dic["Chemical"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "의약품",
#                   "messageText": pred_dic["Medicine"]
#                 }
#               ]
#             },
#               {
#               "title": "비금속광물, 철강금속",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EB%B9%84%EA%B8%88%EC%86%8D%EA%B4%91%EB%AC%BC,%EC%B2%A0%EA%B0%95%EA%B8%88%EC%86%8D.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "비금속광물",
#                   "messageText": pred_dic["Non_Metal"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "철강금속",
#                   "messageText": pred_dic["Metal"]
#                 }
#               ]
#             },
#               {
#               "title": "기계, 전기전자",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EA%B8%B0%EA%B3%84,%EC%A0%84%EA%B8%B0%EC%A0%84%EC%9E%90.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "기계",
#                   "messageText": pred_dic["Machine"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "전기전자",
#                   "messageText": pred_dic["Electronic"]
#                 }
#               ]
#             },
#               {
#               "title": "건설업, 운수창고",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EA%B1%B4%EC%84%A4%EC%97%85,%EC%9A%B4%EC%88%98%EC%B0%BD%EA%B3%A0.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "건설업",
#                   "messageText": pred_dic["Construction"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "운수창고",
#                   "messageText": pred_dic["Transport"]
#                 }
#               ]
#             },
#               {
#               "title": "유통업, 전기가스업",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%9C%A0%ED%86%B5%EC%97%85,%EC%A0%84%EA%B8%B0%EA%B0%80%EC%8A%A4%EC%97%85.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "유통업",
#                   "messageText": pred_dic["Distribution"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "전기가스업",
#                   "messageText": pred_dic["Power"]
#                 }
#               ]
#             },
#               {
#               "title": "통신업, 금융업",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%ED%86%B5%EC%8B%A0%EC%97%85,%EA%B8%88%EC%9C%B5%EC%97%85.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "통신업",
#                   "messageText": pred_dic["Tele"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "금융업",
#                   "messageText": pred_dic["Finance"]
#                 }
#               ]
#             },
#               {
#               "title": "증권, 보험",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%A6%9D%EA%B6%8C,%EB%B3%B4%ED%97%98.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "증권",
#                   "messageText": pred_dic["Brokerage"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "보험",
#                   "messageText": pred_dic["Insurer"]
#                 }
#               ]
#             },
#               {
#               "title": "서비스업, 제조업",
#               "description": str(datetime.datetime.now()+datetime.timedelta(days=1,hours=9))[5:10]+" 일자 업종 시세 예상 추이 확인",
#               "thumbnail": {
#                 "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%84%9C%EB%B9%84%EC%8A%A4%EC%97%85,%EC%A0%9C%EC%A1%B0%EC%97%85.png?raw=true"
#               },
#               "buttons": [
#                 {
#                   "action": "message",
#                   "label": "서비스업",
#                   "messageText": pred_dic["Service"]
#                 },
#                 {
#                   "action":  "message",
#                   "label": "제조업",
#                   "messageText": pred_dic["Manufacturer"]
#                 }
#               ]
#             }
#           ]
#         }
#       }
#     ]
#   }
# }

#     # 답변 전송
#     return jsonify(response)

# if __name__ == "__main__":
#     application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------



import import_ipynb

import UTDdata2
import 전처리2
import TomorrowPredict