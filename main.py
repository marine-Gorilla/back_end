from fastapi import FastAPI, HTTPException
import requests
from model import MemberInfo
import json

app = FastAPI()

@app.post("/send_to_kakao/")
async def send_to_kakao(member_info: MemberInfo):
    # 여러분의 Kakao API 인증 정보 및 필요한 세부 정보
    kakao_api_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    kakao_access_token = "<여러분의 Kakao Access Token>"

    headers = {
        "Authorization": f"Bearer {kakao_access_token}"
    }

    # KakaoTalk에 보낼 메시지 구성
    message = f"이름: {member_info.name}\n생년월일:{member_info.berth}\n주소:{member_info.address}이메일: {member_info.email}\n메시지: {member_info.message}"

    payload = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://yourwebsite.com",
                "mobile_web_url": "https://yourwebsite.com"
            }
        })
    }

    # Kakao API로 POST 요청 보내기
    response = requests.post(kakao_api_url, headers=headers, data=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="KakaoTalk으로 메시지 전송에 실패했습니다")

    return {"status": "메시지 전송 성공"}
