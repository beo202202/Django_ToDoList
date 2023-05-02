<h1>6주차~7주차 장고 심화 과제</h1>
<h2> DRF로 ToDoList 만들기</h2>
<br>
<h3>구현 기능</h3>
<h4>USERS</h4>
<li>회원가입(POST) : 필수 필드(id, email, password, name, gender, age, introduntion)</li>
<li>로그인(POST)</li>
<li>로그아웃(POST) : 미구현</li>
<li>회원 정보 수정(PUT)</li>
<li>회원 탈퇴(DELETE)</li>
<br>
<h4>TODO</h4>
<li>할일 만들기(POST) : 필수 필드(id, title, is_complete, created_at, updated_at, completion_at, user_id(FK))</li>
<li>할일 목록 조회(GET)</li>
<li>할일 수정(PUT)</li>
<li>할일 삭제(DELETE)</li>
<br>
<h4>추가</h4>
<li>작성자 본인만 조회, 수정, 삭제 가능</li>
<li>JWT 방식 : accesss 토큰 payload 정보(user email, name, gender, age)</li>
<li>test코드: 로그인, 로그아웃</li>
<br>
<h4>ERD Cloud</h4>

![image](https://user-images.githubusercontent.com/125543130/235286201-ff46c992-b503-4e68-a5a7-1a57169c31d8.png)
