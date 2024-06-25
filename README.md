# 텔레그램 봇에 메시지 보내는 방법

## 봇을 만든다.

### Bot Father 를 검색해서 들어간다.

### 봇을 만든다

### Token을 기억한다.

## 채팅 ID를 가져온다.

### 공통
`https://api.telegram.org/bot{token}/getUpdates`
- 위 링크에 Bot Father로부터 발급받은 token을 넣어준다.
- 예시) `https://api.telegram.org/botmyTestToken123/getUpdates`


### 봇과의 개인 챗
- 말을 건다
- 위 링크를 새로고침 한다
    - 또는 아래 함수를 실행해서 chat id를 가져온다.

### 채널에 추가한 봇
- 채널에 추가한다
- 위 링크를 새로고침 한다
    - 또는 아래 함수를 실행해서 chat id를 가져온다.