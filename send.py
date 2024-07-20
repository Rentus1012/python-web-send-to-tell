from twilio.rest import Client

# 문자 API id + token
#account_sid = <API_ID>
#auth_token  = <TWILIO_TOKEN>
client = Client(account_sid, auth_token)

 # 걸러진 전화번호를 저장하여 message API 사용
message = client.messages.create(
        to='+82'+ PHONE_NUMBER, 
        from_="<SERVER_PHONE_NUMBER>",
        body="<메세지 내용>"
)