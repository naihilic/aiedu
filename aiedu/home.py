import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Label, HBox, VBox, HTML
from IPython.display import YouTubeVideo
# a talk about IPython at Sage Days at U. Washington, Seattle.
# Video credit: William Stein.

courses = { "프로그래밍": {
              "Python": {
                "Python 기초": { "desc": "blah" },
                "Python 실습": { "desc": "blah" },
                "Python 고급": { "desc": "blah" }
              },
              "Java": {},
              "C/C++": {},
              "Go": {}
            },
            "인공지능": {
            },
            "데이터분석": {
            },
            "클라우드": {
              "도커": {},
              "Kubernetes": {}
            }
}

questions = { 'q1': {'type': 'select', 'question': '바람이 패배한 이유는?', 'choices': ['노력', '전략', '계절', '확률']},
              'q2': {'type': 'select', 'question': '토끼가 간을 잃어버린 이유는?', 'choices': ['그런 일 없음', '실수', '건망증', '천재지변']},
              'q3': {'type': 'select', 'question': '임베딩을 하는 이유는?', 'choices': ['재밌음', '멋있음', '신기함', '학습에 도움이 됨']},
              'q4': {'type': 'select', 'question': '커피를 마셔야 하는 때는?', 'choices': ['배고플 때', '잠자기 전', '조깅 중', '좋은 날']}
}

courseCurr = { 'title': 'NA',
                'videos': ['Nxz6FxGH_6U','',''],
                'summaries': ['rc/a.html', 'rc/b.html'],
                'questions': ['q1','q2','q3','q4'],
                'references': ['r1.html', 'r2.html']
             }

videos = [ {'subject': '자전거를 배우자', 'vid': 'Nxz6FxGH_6U'},
           {'subject': '노래를 배우자', 'vid': '2D5cmNyd0R0'},
           {'subject': '우체국에 가보자', 'vid': 'dIY6y5f98qk'}]

def on_summary_clicked(b):
    b.output.clear_output()
    with b.output:
        courseCurr['idxSummary'] = 0 if 'idxSummary' not in courseCurr.keys() else courseCurr['idxSummary']+(1 if b.action=='next' else -1)
        #print(f'Button clicked - Action[{b.action}] - idx: {courseCurr["idxSummary"]}')
        courseCurr['idxSummary'] = 0 if courseCurr['idxSummary'] <=0 else (len(courseCurr['summaries'])-1 if courseCurr['idxSummary']>=len(courseCurr['summaries']) else courseCurr['idxSummary'])
        urlPage = courseCurr['summaries'][courseCurr['idxSummary']]
        with open(urlPage) as f:
            strSummary = f.read()
            display(HTML(value=strSummary))

def on_test_clicked(b):
    b.output.clear_output()
    with b.output:
        courseCurr['idxQuestion'] = 0 if 'idxQuestion' not in courseCurr.keys() else courseCurr['idxQuestion']+(1 if b.action=='next' else -1)
        courseCurr['idxQuestion'] = 0 if courseCurr['idxQuestion'] <=0 else (len(courseCurr['questions'])-1 if courseCurr['idxQuestion']>=len(courseCurr['questions']) else courseCurr['idxQuestion'])
        qid = courseCurr['questions'][courseCurr['idxQuestion']]
        print(f'문제 : {questions[qid]["question"]}')
        for idx, choice in enumerate(questions[qid]['choices']):


            print(f'{idx}. {choice}')

titles = ['1.과정선택', '2.동영상 강의', '3.요약정리', '4.테스트', '5.참고자료']

def init():
    tab = widgets.Tab(titles=['title:'+str(i) for i in range(len(titles))])
    tab.children = [widgets.Output() for title in titles]
    [tab.set_title(i, title) for i, title in enumerate(titles)]

    with tab.children[0]:
      topicsL1 = widgets.Select( options=courses.keys(), value=list(courses.keys())[0], description='', disabled=False) # rows=10,  
      topicsL2 = widgets.Select( options=courses[list(cousrses.keys())[0]].keys(), value=list(courses[list(cousrses.keys())[0]].keys())[0], description='', disabled=False) # rows=10,  
      topicsL3 = widgets.Select( options=['Foo', 'Bar', 'Blah'], value='Foo', description='', disabled=False) # rows=10,  
      display(HBox([VBox([Label(value='대분류'), topicsL1]),
                    VBox([Label(value='중분류'), topicsL2]),
                    VBox([Label(value='소분류'), topicsL3])]))
    with tab.children[1]:
      labelCourse = Label(value='과정명: '+courseCurr['title'])
      display(labelCourse)

      outputVideos = [widgets.Output() for video in videos]
      for idx, outputVideo in enumerate(outputVideos):
        with outputVideo:
            display(YouTubeVideo(videos[idx]['vid']))
      #[videos[idx].display(YouTubeVideo(vid)) for idx, vid in enumerate(vids)]
      accordion = widgets.Accordion(children=outputVideos)
      [accordion.set_title(idx, video['subject']) for idx, video in enumerate(videos)]
      display(accordion)
      #print('아코디언 형태로 비디오 목록 보여주면 좋을듯...')
      #display(YouTubeVideo('Nxz6FxGH_6U'))

    with tab.children[2]:
      labelCourse = Label(value='과정명: '+courseCurr['title'])
      outputContent = widgets.Output()
      btnPrev = widgets.Button(description='이전')
      btnPrev.action = 'prev'
      btnPrev.output = outputContent#tab.children[2]
      btnPrev.on_click(on_summary_clicked)
      btnNext = widgets.Button(description='다음')
      btnNext.action = 'next'
      btnNext.output = outputContent#tab.children[2]
      btnNext.on_click(on_summary_clicked)
      display(VBox([labelCourse,outputContent,HBox([btnPrev, btnNext])]))

    with tab.children[3]:
      labelCourse = Label(value='과정명: '+courseCurr['title'])
      outputContent = widgets.Output()
      btnPrev = widgets.Button(description='이전')
      btnPrev.action = 'prev'
      btnPrev.output = outputContent#tab.children[2]
      btnPrev.on_click(on_test_clicked)
      btnNext = widgets.Button(description='다음')
      btnNext.action = 'next'
      btnNext.output = outputContent#tab.children[2]
      btnNext.on_click(on_test_clicked)
      display(VBox([labelCourse,outputContent,HBox([btnPrev, btnNext])]))
      #display(outputContent)

    display(tab)
 
