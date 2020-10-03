import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Label, HBox, VBox, HTML
from IPython.display import YouTubeVideo
import json

# a talk about IPython at Sage Days at U. Washington, Seattle.
# Video credit: William Stein.

titles = ['1.과정선택', '2.동영상 강의', '3.요약정리', '4.테스트', '5.참고자료']
courses = json.load(open("rc/courses.json"))
#questions = json.load(open("rc/questions.json"))
#videos = josn.load(open("rc/videos.json"))

courseCurr = courses['프로그래밍']['Python']['Python 기초'];

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
    courseCurr['questions'] = json.load(open(courseCurr['questionFile']))
    with b.output:
        courseCurr['idxQuestion'] = 0 if 'idxQuestion' not in courseCurr.keys() else courseCurr['idxQuestion']+(1 if b.action=='next' else -1)
        courseCurr['idxQuestion'] = 0 if courseCurr['idxQuestion'] <=0 else (len(courseCurr['questions'])-1 if courseCurr['idxQuestion']>=len(courseCurr['questions']) else courseCurr['idxQuestion'])
        #qid = courseCurr['questions'][courseCurr['idxQuestion']]
        print(f'문제 : {courseCurr["questions"][courseCurr["idxQuestion"]]["question"]}')
        for idx, choice in enumerate(courseCurr["questions"][courseCurr["idxQuestion"]]['choices']):
            print(f'{idx}. {choice}')

def on_topicL1_change(change):
    global courseCurr
    outputDesc = courseCurr['outputDesc']
    courseL1 = courses[change['new']]
    courseL2 = courseL1[list(courseL1.keys())[0]]
    courseCurr = courseL2[list(courseL2.keys())[0]]
    courseCurr['outputDesc'] = outputDesc
    outputDesc.clear_output()
    with outputDesc:
          display(HTML("<h1>간단소개</h1>"))
          display(courseCurr['description'])
            
def init():
    tab = widgets.Tab(titles=['title:'+str(i) for i in range(len(titles))])
    tab.children = [widgets.Output() for title in titles]
    [tab.set_title(i, title) for i, title in enumerate(titles)]

    with tab.children[0]:
      courseCurr['outputDesc'] = widgets.Output()
      topicsL1 = widgets.Select( options=courses.keys(), value=list(courses.keys())[0], description='', disabled=False) # rows=10,
      topicsL1.observe(on_topicL1_change, names='value')
      topicsL2 = widgets.Select( options=courses[list(courses.keys())[0]].keys(), value=list(courses[list(courses.keys())[0]].keys())[0], description='', disabled=False) # rows=10,  
      topicsL3 = widgets.Select( options=['Foo', 'Bar', 'Blah'], value='Foo', description='', disabled=False) # rows=10,
      with courseCurr['outputDesc']:
          display(HTML("<h2>간단소개</h2>"))
          display(courseCurr['description'])
      display(HBox([VBox([Label(value='대분류'), topicsL1]),
                    VBox([Label(value='중분류'), topicsL2]),
                    VBox([Label(value='소분류'), topicsL3])]))
      display(courseCurr['outputDesc'])
    with tab.children[1]:
      #labelCourse = Label(value='과정명: '+courseCurr['title'])
      display(HTML(f'<h2>과정명: {courseCurr["title"]}</h2>'))

      outputVideos = [widgets.Output() for video in courseCurr['videos']]
      for idx, outputVideo in enumerate(outputVideos):
        with outputVideo:
            display(YouTubeVideo(courseCurr['videos'][idx]['vid']))
      #[videos[idx].display(YouTubeVideo(vid)) for idx, vid in enumerate(vids)]
      accordion = widgets.Accordion(children=outputVideos)
      [accordion.set_title(idx, video['subject']) for idx, video in enumerate(courseCurr['videos'])]
      display(accordion)
      #print('아코디언 형태로 비디오 목록 보여주면 좋을듯...')
      #display(YouTubeVideo('Nxz6FxGH_6U'))

    with tab.children[2]:
      display(HTML(f'<h2>과정명: {courseCurr["title"]}</h2>'))
      #labelCourse = Label(value='과정명: '+courseCurr['title'])
      outputContent = widgets.Output()
      with outputContent:
          display("[다음]버튼을 눌러서 시작해주세요.")
      btnPrev = widgets.Button(description='이전')
      btnPrev.action = 'prev'
      btnPrev.output = outputContent#tab.children[2]
      btnPrev.on_click(on_summary_clicked)
      btnNext = widgets.Button(description='다음')
      btnNext.action = 'next'
      btnNext.output = outputContent#tab.children[2]
      btnNext.on_click(on_summary_clicked)
      display(VBox([outputContent,HBox([btnPrev, btnNext])]))

    with tab.children[3]:
      #labelCourse = Label(value='과정명: '+courseCurr['title'])
      display(HTML(f'<h2>과정명: {courseCurr["title"]}</h2>'))
      outputContent = widgets.Output()
      with outputContent:
          display("[다음]버튼을 눌러서 시작해주세요.")
      btnPrev = widgets.Button(description='이전')
      btnPrev.action = 'prev'
      btnPrev.output = outputContent#tab.children[2]
      btnPrev.on_click(on_test_clicked)
      btnNext = widgets.Button(description='다음')
      btnNext.action = 'next'
      btnNext.output = outputContent#tab.children[2]
      btnNext.on_click(on_test_clicked)
      display(VBox([outputContent,HBox([btnPrev, btnNext])]))
      #display(outputContent)

    display(tab)
 
