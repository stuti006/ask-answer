from django.shortcuts import redirect, render,HttpResponse
from django.http import JsonResponse
from .models import Question,Answer,Comment,UpVote,DownVote
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import AnswerForm,QuestionForm
# from .forms import AnswerForm,QuestionForm,ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count



from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

import collections.abc, datetime, base64, binascii, re, sys, types

# bot= ChatBot('chatBot' ,read_only= False,
# logic_adapters= [
#     {
#         'import_path' : 'chatterbot.logic.BestMatch',
#         'default_response' : '''You get your answers on <a href="/home ">ASK_US</a> ''',
#         'maximum_similarity_threshold' : 0.90
                     
                    
#     }            
#             ])
        

  
# list_to_train = [
#        "hi",
#        "hi, there",
#        " What's your name?",
#        "I'm just a chatbot",
#        "yes",
#     #    "Okay",
#     #    "Thank You",
#     #    "Your Welcome 😄",   
#     #    "How many exams are conducted yearly?",
#     #    "4-Internal Assessment  and 2-end semesters",
#     #    "is scholarship scheme open for all students enrolled in this college?",
#     #    "No. It is only available for students under OBC, SC/ST/NT category and also for EBC students.",
#     #    "can the students apply for scholarship scheme anytime during the course?",
#     #    "No , they can only apply in the first year.",
#     #    "can the students cancel the scholarship scheme after applying for it?",
#     #    "yes they are ",
#     #    "Are foreign students eligible for scholarship scheme?",
#     #    "NO",
#     #    "What all documents are required to apply for scholarship?",
#     #    "income cerWhat all documents are required to apply for scholarship?tificate, domicile certificate,declaration form,ration card, caste validity and caste certificate(for students under SC/SC/OBC/NT category), CAP allotment form.",
#     #    "What is the fees structure for OBC category students?",
#     #    "it is half of the total amount.If you want to know your specific fee strucute, you can mail your detials  at @principle.rait.in ",
#     #    "What is the fee structure for SC/ST/NT category students?",
#     #    "it is 20 of the total amount",
#     #    "Which entrance exam does RAIT college accept?",
#     #    "RAIT college accepts MHT CET, JEE-MAIN, GATE.",
#     #    "What all documents are required to apply for scholarship?",
#     #    "income certificate, domicile certificate,declaration form,ration card, caste validity and caste certificate(for students under SC/SC/OBC/NT category), CAP allotment form.",
#     #    "What is the fee structure for Open category students?",
#     #    "1,39,999 yearly",
#     #    "is it allowed to pay Fee in installments?",
#     #    "yes you can pay fees in installments if the amount is high.",
#     #    "What is the fees for M.E and ph.D?",
#     #    "1.5 lakhs(1st year fees) for M.E and 2 lakhs (1st year fees) for ph.D.",
#     #    "What documents are generally required at the time of the admission?",
#     #    "10th and 12th makrsheet, JEE/MHCET marksheet, CAP allotment form, leaving certificate, caste certificate",
#     #    "How can i get admission for UG in RAIT?",
#     #    "Admissions in UG programme are on the basis of MH CET and JEE-MAIN scorecard.",
#     #    "What is the admission criteria for RAIT?",
#     #    "For the admissions in UG courses or PG courses, candidates must have minimum aggregate of 50 in the last qualifying examination.",
#     #    "What is the selection criteria for admission in MTech at RAIT?",
#     #    "Admission in MTech is based on scores obtained in the GATE.",
#     #    "Which companies mostly recruits rait students?",
#     #    "TCS, CISCO, TIAA, JP Morgan,LnT Infotech etc.",
#     #    "what was the highest package offered in RAIT?",
#     #    "it depends on your skills and the recruting company.In 2020 16LPA was the highest package offered",
#     #    "What is the average package offered in RAIT?",
#     #    "Average package varies every year and it can go upto 4 LPA , 6LPA etc.",
#     #    "What is the institute rank in terms of placement?",
#     #    "The institute is ranked '9' under placements.",
#     #    "Is RAIT approved by AICTE?",
#     #    "Yes, RAIT is approved by AICTE",
#     #    "Which all committees are there  in rait?",
#     #    "SUC, IEEE, IETE,CSI,ACM,ISTE,Kalaraag, codechef, Motif",
#     #    "how many courses are available under B.Tech ?",
#     #    "Electronics, IT,CS,Electronics and telecommunication, Instrumentation",
#     #    "Are the classrooms Air Conditioned?",
#     #    "yes some of them are Air Conditioned",
#     #    "Is production engineering and automobile engineering course available?",
#     #    "no it is not",
#     #    "Is chemical , civil and mechanical engineering courses available?",
#     #    "NO ,not there",
#     #    "Is there any transport Facility available for students?",
#     #    "Not yet",
#     #    "What are the timings for classes ?",
#     #    "8:30 to 4:30",
#     #    "Is there any Hostel facility available?",
#     #    "yes Hostel facility is available and it can accomodate large number of girls and boys",
#     #    "What is the NAAC grade of RAIT?",
#     #    "RAIT is accredited with 'A' Grade by NAAC",
#     #    "What are the courses available in this college?",
#     #    "B.E/M.E/ph.D",
#        "How many fest are there?",
#        "Two. Technical and Non-technical ",
#        "Fest happens during which  time of the year?",
#        "September-october and March"
   



#   ]

# chatterbotCorpusTrainer =  ChatterBotCorpusTrainer(bot)

# # list_trainer = ListTrainer(bot)
# # list_trainer.train(list_to_train)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')






def index(request):
    return render(request,'main/index.html')
# Create your views here.

def bott(request):
    return render(request,'main/bott.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

def internship1(request):
    return render(request,'main/internship1.html')

def internship2(request):
    return render(request,'main/internship2.html')

def internship3(request):
    return render(request,'main/internship3.html')

def workshop1(request):
    return render(request,'main/workshop1.html')

def workshop2(request):
    return render(request,'main/workshop2.html')

def workshop3(request):
    return render(request,'main/workshop3.html')

def workshop4(request):
    return render(request,'main/workshop4.html')

def events1(request):
    return render(request,'main/events1.html')

def events2(request):
    return render(request,'main/events2.html')

def events3(request):
    return render(request,'main/events3.html')

# Home Page
def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(title__icontains=q).order_by('-id')
    else:
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')
    paginator=Paginator(quests,4)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'main/home.html',{'quests':quests})

# Detail
def detail(request,id):
    # quest=Question.objects.get(pk=id)
    # tags=quest.tags.split(',')

    # return render(request,'detail.html',{
    #     'quest':quest,
    #     'tags':tags,
    #     'answers':answers,
    #     'answerform':answerform
    # })
    quest=Question.objects.get(pk=id)
    tags = quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
            messages.success(request,'Answer has been submitted.')

    # quest = Question.objects.all(pk=id)
    return render(request,'main/detail.html',{
        'quest':quest,
        'tags':tags,
        'answers':answers,
        'answerform':answerform
    })

# # Save Comment
def save_comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool':True})

# # Save Upvote
def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=UpVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# # Save Downvote
def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=DownVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            DownVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# User Register
def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered!!')
    return render(request,'registration/register.html',{'form':form})

# # Ask Form
def ask_form(request):
    form=QuestionForm
    if request.method=='POST':
        questForm=QuestionForm(request.POST)
        if questForm.is_valid():
            questForm=questForm.save(commit=False)
            questForm.user=request.user
            questForm.save()
            messages.success(request,'Question has been added.')
    return render(request,'main/ask-question.html',{'form':form})


# Questions according to tag
def tag(request,tag):
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'main/tag.html',{'quests':quests,'tag':tag})

# # Profile
# def profile(request):
#     quests=Question.objects.filter(user=request.user).order_by('-id')
#     answers=Answer.objects.filter(user=request.user).order_by('-id')
#     comments=Comment.objects.filter(user=request.user).order_by('-id')
#     upvotes=UpVote.objects.filter(user=request.user).order_by('-id')
#     downvotes=DownVote.objects.filter(user=request.user).order_by('-id')
#     if request.method=='POST':
#         profileForm=ProfileForm(request.POST,instance=request.user)
#         if profileForm.is_valid():
#             profileForm.save()
#             messages.success(request,'Profile has been updated.')
#     form=ProfileForm(instance=request.user)
#     return render(request,'registration/profile.html',{
#         'form':form,
#         'quests':quests,
#         'answers':answers,
#         'comments':comments,
#         'upvotes':upvotes,
#         'downvotes':downvotes,
#     })

# Tags Page
def tags(request):
    quests=Question.objects.all()
    tags=[]
    for quest in quests:
        qtags=[tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count=[]
    for tag in tags:
        tag_data={
            'name':tag,
            'count':Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)
    return render(request,'main/tags.html',{'tags':tag_with_count})
        
        