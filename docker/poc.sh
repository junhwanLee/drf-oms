#!/bin/sh 

##
# 회원 가입 
## 
curl --location --request POST 'http://localhost:8080/accounts/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "youngmi@test.com",
    "password": "Jhlee'\''spwd0",
    "name": "정영미",
    "nickname": "yougmi",
    "phone": "01083574361"
}'


curl --location --request POST 'http://localhost:8080/accounts/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "leecg@test.com",
    "password": "Jhlee'\''spwd0",
    "name": "이철근",
    "nickname": "leecg",
    "phone": "01083574362"
}'


curl --location --request POST 'http://localhost:8080/accounts/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dream@test.com",
    "password": "Jhlee'\''spwd0",
    "name": "이은겸",
    "nickname": "dream",
    "phone": "01083574363"
}'

curl --location --request POST 'http://localhost:8080/accounts/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "sungi@test.com",
    "password": "Jhlee'\''spwd0",
    "name": "김선기",
    "nickname": "sungi",
    "phone": "01083574364"
}'


##
# 회원 로그인
## 
USER1=`curl --location --request POST 'http://localhost:8080/auth/login' \
--header 'Content-Type: application/json' \
--data-raw '{
	"email": "sungi@test.com", 
	"password" : "Jhlee'\''spwd0"
}'`

USER2=`curl --location --request POST 'http://localhost:8080/auth/login' \
--header 'Content-Type: application/json' \
--data-raw '{
	"email": "sungi@test.com", 
	"password" : "Jhlee'\''spwd0"
}'`

# 사용자의 token 값 저장
USER1_TOKEN=`echo $USER1 | jq -r '.token'`
USER2_TOKEN=`echo $USER2 | jq -r '.token'`

# 사용자의ID값 저장 
USER1_ID=`echo $USER1 | jq -r '.user.id'`
USER2_ID=`echo $USER2 | jq -r '.user.id'`

##
# 주문목록 등록
## 

# USER1 상품 등록
curl --location --request POST 'http://localhost:8080/orders/' \
--header 'Authorization: Token '$USER1_TOKEN'' \
--header 'Content-Type: application/json' \
--data-raw '{
	"customer": '$USER1_ID',
	"order_number" : "020602134001",
	"product_name" : "무지개 미니낭초"
}'

curl --location --request POST 'http://localhost:8080/orders/' \
--header 'Authorization: Token '$USER1_TOKEN'' \
--header 'Content-Type: application/json' \
--data-raw '{
	"customer": '$USER1_ID',
	"order_number" : "020602140001",
	"product_name" : "오크 스탠다느 수납장"
}'

# USER2 상품 등록
curl --location --request POST 'http://localhost:8080/orders/' \
--header 'Authorization: Token '$USER2_TOKEN'' \
--header 'Content-Type: application/json' \
--data-raw '{
	"customer": '$USER2_ID',
	"order_number" : "020602134002",
	"product_name" : "[신메뉴할인] 꼬막무침"
}'

curl --location --request POST 'http://localhost:8080/orders/' \
--header 'Authorization: Token '$USER2_TOKEN'' \
--header 'Content-Type: application/json' \
--data-raw '{
	"customer": '$USER2_ID',
	"order_number" : "020602150002",
	"product_name" : "무색소 천연가루 마카롱"
}'

## 
# 회원 로그아웃
##

# USER1 사용자 로그아웃 
curl --location --request POST 'http://localhost:8080/auth/logout' \
--header 'Authorization: Token '$USER1_TOKEN'' \
--header 'Content-Type: application/json' \
--data-raw ''

##
# 단일 회원 상세 정보 조회
## 

curl --location --request GET 'http://localhost:8080/accounts/users/'$USER2_ID'' \
--header 'Authorization: Token '$USER2_TOKEN'' \
--header 'Content-Type: application/json' \
--data-raw ''


##
# 단일 회원의 주문 목록 조회 
##
curl --location --request GET 'http://localhost:8080/orders/' \
--header 'Authorization: Token '$USER2_TOKEN'' \
--data-raw ''

##
# 여러회원 목록 조회
##

# search param 에 이메일 또는 이름으로 검색
# last_order 필드에 마지막 주문목록이 노출 됨.
curl --location --request GET 'http://localhost:8080/accounts/users?search=test.com' \
--header 'Authorization: Token 'USER2_TOKEN'' \
--data-raw ''
