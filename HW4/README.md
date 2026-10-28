# HW4 : todo 앱에 API 더하기

## 더한 것

- 설명 칸(`note`)을 API로 주고받습니다. 생략하면 빈 문자열로 저장합니다.
- `GET /api/todos/?done=true`는 완료한 것만, `?done=false`는 미완료만 반환합니다. 조건을 생략하면 전체 목록을 반환합니다.
- PATCH는 보낸 칸만 수정하고, PUT은 보내지 않은 `done`과 `note`를 기본값으로 되돌립니다.
- Swagger UI에 note 필드와 done 쿼리 입력 칸을 표시합니다.

## 실행하는 법

저장소의 최상위 폴더에서 실행합니다.

```bash
source venv/bin/activate
cd HW4
python -m pip install -r requirements.txt
flask --debug run
```

가상환경이 없다면 먼저 저장소 최상위 폴더에서 `python3 -m venv venv`로 만듭니다.

- 화면: http://127.0.0.1:5000/
- API 문서: http://127.0.0.1:5000/api/docs
- Swagger JSON: http://127.0.0.1:5000/api/swagger.json

처음 실행하면 `HW4/instance/todo.db`가 생성됩니다. 기존 실습의 DB를 복사하지 않습니다.
`instance/`, `venv/`, Python 캐시는 Git에서 제외합니다.

## 테스트

HW4 폴더에서 실행합니다. 서버를 켤 필요가 없습니다.

```bash
python -m unittest -v
```

5개 테스트가 생성·목록·부분 수정·삭제·404 응답을 확인합니다.

테스트마다 `create_app()`에 메모리 DB 설정을 전달합니다. SQLAlchemy 연결 **전에** 설정하므로 실제 `instance/todo.db`를 사용하거나 삭제하지 않습니다. Flask CLI는 `create_app`을 자동으로 찾아 실행합니다.

## 화면

아래 이미지는 실제 Swagger UI에서 요청을 실행한 화면입니다. 캡처에는 별도의 메모리 DB와 포트 5054를 사용했습니다. 일반 실행 포트는 5000입니다.

### 1. 주소 여섯 줄이 모두 보이는 문서

![docs](docs.png)

### 2. note를 넣어 만들었더니 201이 온 모습

![post](post.png)

### 3. 없는 번호를 불렀더니 404가 온 모습

![404](notfound.png)
