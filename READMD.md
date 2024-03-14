# YGO_Blog

---

## 개요

---

### 1.1 개요

---

YGO Blog는 제가 좋아하는 게임중 하나인 유희왕에 대해 정보 공유를 할 수 있게 만들어진 Blog입니다.

사용자들이 글을 올리는 게시판 형태의 Blog와,
게임 정보 목적으로 사용하는 Decks로 나뉘어져 있습니다.

### 1.2 기능

Main

- 메인
- 현재 계정정보 조회
- 회원가입
- 로그인
- 로그아웃

Blog

- 게시글 작성, 수정, 삭제
- 댓글, 대댓글 작성, 수정, 삭제
- 게시글 검색 by category

- 삭제된 게시글 복구

Decks

- 덱 포스트 작성, 수정, 삭제
- 매치 기록 작성, 수정, 삭제

### 1.3 개발환경

- vscode
- django framework
- python

- html, css, js
- bootstrap

- git, github

#### WBS

```mermaid
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section 기획
    컨셉 기획           :2024-03-07, 2d
    section FE
    화면 기획      :2024-03-9  , 1d
    wireframe 제작 : 2024-03-10, 2d
    부트스트랩 적용 : 2024-03-11, 2d
    section BE
    URL 구조 기획   : 2024-03-08, 2d
    CRUD 구현   : 2024-03-09, 1d
    인증 구현   : 2024-03-10, 1d
    Blog 구현   : 2024-03-09, 3d
```

## 설계

---

### Wireframe

![list](https://media.discordapp.net/attachments/1111153532184301630/1217623417797476495/blog_Untitled_1.png?ex=6604b32d&is=65f23e2d&hm=fbfc5c7923dbccf0af9849a7f0f61b8a6f5e85c4db5c3129e1c68e0b3b33dbd8&=&format=webp&quality=lossless&width=1352&height=676)

---

### 실제 화면

- 메인 페이지

![list](https://media.discordapp.net/attachments/1111153532184301630/1217642707208503411/image.png?ex=6604c524&is=65f25024&hm=9074b49d1353453a5439d17b91cbb43e572fcc6f3ccee49c1ea4ecd630d67d59&=&format=webp&quality=lossless&width=1007&height=676)

- 덱 리스트

![list](https://media.discordapp.net/attachments/1111153532184301630/1217633799307788288/image.png?ex=6604bcd8&is=65f247d8&hm=b81df4e7c15f879c9080e0f0233e2a44169f57deb00fefa0306d5eebaa321caa&=&format=webp&quality=lossless)

- 덱 상세

![list](https://media.discordapp.net/attachments/1111153532184301630/1217643815259734027/image.png?ex=6604c62c&is=65f2512c&hm=87704d11083822fc1612a9e55b4088012d7e7046852a49101dbfc103b3abd5c6&=&format=webp&quality=lossless&width=1057&height=676)

### URL 구조

---

| App    | URL                                       | Views                        | Html                      | Note                                   |
|--------|-------------------------------------------|------------------------------|---------------------------|----------------------------------------|
| Admin  | 'admin/'                                  | Django admin                 | Django admin templates    | Django 관리자 인터페이스                |
| Main   | ''                                        | MainView                     | index.html                | 메인 페이지                             |
|        | 'register/'                               | RegisterView                 | register.html             | 회원가입 페이지                         |
|        | 'login/'                                  | LoginView                    | login.html                | 로그인 페이지                           |
|        | 'logout/'                                 | LogoutView                   | redirect to main          | 로그아웃 액션, 메인으로 리다이렉트       |
|        | 'account/<int:pk>/'                       | AccountView                  | account.html              | 사용자 계정 상세 페이지                  |
| Blog   | 'blog/'                                   | BlogListView                 | blog_list.html            | 블로그 리스트 페이지                    |
|        | 'blog/<int:pk>/'                          | BlogDetailView               | blog_detail.html          | 블로그 상세 페이지                      |
|        | 'blog/write/'                             | PostCreateView               | blog_write.html           | 블로그 작성 페이지                      |
|        | 'blog/edit/<int:pk>/'                     | PostUpdateView               | blog_write.html           | 블로그 수정 페이지                      |
|        | 'blog/delete/<int:pk>/'                   | PostDeleteView               | redirect to blog list     | 블로그 삭제 액션, 리스트로 리다이렉트    |
|        | 'blog/search/<str:category>/'             | BlogSearchView               | blog_search_list.html     | 블로그 카테고리 검색 결과 페이지         |
|        | 'blog/restore/<int:pk>/'                  | PostRestoreView              | redirect to blog detail   | 삭제된 블로그 복구 액션                  |
|        | 'blog/comment/write/<int:pk>/'            | CreateCommentView            | redirect to blog detail   | 댓글 작성 액션                           |
|        | 'blog/comment/edit/<int:comment_pk>/'     | UpdateCommentView            | redirect to blog detail   | 댓글 수정 액션                           |
|        | 'blog/comment/delete/<int:comment_pk>/'   | DeleteCommentView            | redirect to blog detail   | 댓글 삭제 액션                           |
|        | 'blog/subcomment/write/<int:comment_pk>/' | CreateSubCommentView         | redirect to blog detail   | 대댓글 작성 액션                         |
|        | 'blog/subcomment/edit/<int:subcomment_pk>/' | UpdateSubCommentView       | redirect to blog detail   | 대댓글 수정 액션                         |
|        | 'blog/subcomment/delete/<int:subcomment_pk>/' | DeleteSubCommentView     | redirect to blog detail   | 대댓글 삭제 액션                         |
| Decks  | 'decks/'                                  | DeckListView                 | deck_list.html            | 덱 리스트 페이지                        |
|        | 'decks/<int:pk>/'                         | DeckDetailView               | deck_detail.html          | 덱 상세 페이지                          |
|        | 'decks/create/'                           | DeckPostCreateView           | deck_create.html          | 덱 포스트 작성 페이지                   |
|        | 'decks/match_records/'                    | MatchRecordListView          | match_record_list.html    | 매치 기록 리스트 페이지                 |
|        | 'decks/match_records/<int:pk>/'           | MatchRecordDetailView        | match_record_detail.html  | 매치 기록 상세 페이지                   |
|        | 'decks/match_records/create/'             | MatchRecordCreateView        | match_record_create.html  | 매치 기록 작성 페이지                   |

### ER Diagram

---

```mermaid
erDiagram
    User {
        str user_name UK
        str email
        str password
    }

    BlogPost {
        int id PK
        str title
        str author FK
        str category
        str content
        datetime created_at
        bool is_deleted
        int views
        img image
    }

    BlogComment {
        int id PK
        str content
        datetime created_at
        str author FK
        int post FK
    }

    BlogSubComment {
        int id PK
        str content
        datetime created_at
        str author FK
        int comment FK
    }

    DeckPost {
        int id PK
        str title
        str author FK
        str description
        datetime created_at
        bool is_deleted
        img deck_img
    }

    DeckInDeckPost {
        int id PK
        int deck_post FK
        str deck_name FK
    }

    Deck {
        int id PK
        str deck_name UK
    }

    MatchRecord {
        int id PK
        int uid FK
        str tier
        str result
        datetime date
        str description
    }

    MatchDeck {
        int id PK
        int match FK
        str deck_name FK
        bool is_player
    }

    User ||--o{ BlogPost : "author"
    User ||--o{ BlogComment : "author"
    User ||--o{ BlogSubComment : "author"
    User ||--o{ MatchRecord : "uid"
    User ||--o{ DeckPost : "author"
    BlogPost ||--o{ BlogComment : "post"
    BlogComment ||--o{ BlogSubComment : "comment"
    DeckPost ||--o{ DeckInDeckPost : "deck_post"
    DeckInDeckPost ||--|| Deck : "deck_name"
    MatchRecord ||--o{ MatchDeck : "match"
    MatchDeck ||--|| Deck : "deck_name"
```
