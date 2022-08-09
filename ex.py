
daily_news = {
    'all' : ['전체키워드1','전체키워드2','전체키워드3'],
    'negative' : ['부정키워드1','부정키워드2','부정키워드3'],
    'positive' : ['긍정키워드1','긍정키워드2','긍정키워드3']
}


df_sector = {
    'Food':{
        '097950':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '271560':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '000080':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '004370':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/'],
        '005300':['키워드1','키워드2','키워드3','https://www.nate.com/','https://www.naver.com/','https://www.google.co.kr/','https://www.daum.net/','https://tv.kakao.com/']
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
