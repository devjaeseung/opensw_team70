# Team70 업무 분담 및 Git 규칙

- 틀린 그림 찾기 생성하기
    - 원본 이미지에 새로운 이미지 추가하여 틀린 그림찾기의 그림 생성하기
    1. 누끼딴 이미지를 크기 조절하여 원본 이미지 안에 넣고 생성한다. → (성현)
- 틀린 그림을 찾은 후에 어떤 그림인지 객체 탐지하기
    1. 고양이 or 강아지 or 사물 등등.. →(영현)
    2. 얼굴 찾기 → (광규)

### 팀플 내에서 마음껏 개발을 위한 Git 전략


![스크린샷 2023-12-09 21 28 31](https://github.com/devjaeseung/opensw_team70/assets/100324690/1550cb55-d839-42c4-835c-9c1e7e0a7258)

- git fork → clone → branch → push → pull request → pull
    - 팀의 Repository를 나의 개인 Repository로 fork하여 가져온다.
        - 1.Fork a GitHub repository: navigate to a repository on GitHub and click the `Fork` button.
    - 이후 git clone을 통하여 나의 로컬로 가져온다.
        - 2.Clone the repository locally:
            
            ```yaml
            $ git clone https://github.com/devjaeseung/opensw_team70.git
            ```
            
    - 로컬과 팀의 Repository를 연결해둔다. (나중에 팀의 Repository가 업데이트 되었을때를 대비)
        - 3.Add remote called “upstream” pointing to the original repository: .
            
            ```yaml
            $ git remote add upstream https://github.com/devjaeseung/opensw_team70.git
            ```
            
        - 로컬에 remote 연결된 상태를 파악
    - 내가 로컬 작업을 할 branch를 만든다.
        - 4.Checkout a new branch (here called “new_feature”):
            
            ```yaml
            git checkout -b new_feature
            ```
            
        - 5.Make desired changes to the local repository on this branch.
    - 만약 팀 Repository에 변경사항이 있어 코드를 가져오고 싶다면,
        - Pull new changes from remote
            
            ```yaml
            // 팀 main branch로 연결하기.
            $ git checkout main
            
            // 팀의 upstream 당겨서 합치기.
            $ git pull upstream main
            ```
            
        - Sync dev branch (로컬에서 작업하고 있는 branch와 병합하여 싱크를 맞춘다.)
            
            ```yaml
            $ git checkout new_feature
            $ git merge main
            ```
            
        - Push changes to your remote repository (나의 Repository를 연결시킨다.)
            
            ```yaml
            $ git push origin new_feature.
            ```
            
    - 나의 개인 Repository를 본 프로젝트에 Pull request 요청하여 본프로젝트와 합친다.
        - Open a pull request on GitHub merging your changes with the upstream (original) repository. (Pull request 요청)
    - 나의 로컬 프로젝트를 본 프로젝트와 합치고 싶으면, 본 Repository에서 Pull한다.
        - Once the pull request is accepted, you’ll want to pull those changes into your origin (forked repository). 
        Change to master: `git checkout master` and pull: `git pull upstream master`
    - 로컬에서 작업하던 Branch가 작업이 끝나 삭제하고 싶다면,
        - Delete your feature branch using the GitHub website or, delete the local branch: 
        (로컬에서 작업하는 branch 삭제)
            
            ```yaml
            $ git branch -d new_feature
            ```
            
        - and delete the remote:
        (나의 Repository에서 branch 삭제)
            
            ```yaml
            $ git push origin --delete new_feature.
            ```
