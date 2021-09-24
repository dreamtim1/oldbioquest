from . import counter
from .models import Question, Tag, Profile, Solved
from .forms import QuestionForm, SignUpForm
import django.core.exceptions
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    search = request.GET.get('search', '')
    if search:
        return test(request)
    return render(request, 'main/index.html')

def check(request, slug = ''):

    international_part3 = [('ЗЭ', '2021'), ('ЗЭ', '2019'), ('ЗЭ', '2018')]

    if not request.user.is_authenticated:
        return redirect('login')

    search = request.GET.get('search', '')
    if search:
        return test(request)

    if slug == '':
        tagf = True
    else:
        tagf = False

    chpart = request.GET.get('part', 'n')
    chstage = str(request.GET.get('stage', 'all'))[:2]

    part1f = False
    part2f = False
    partnf = False
    auto1 = False
    auto2 = False

    result = ''
    color = ''
    right = ''
    context = {}


    next = False
    i = 0
    k = 1
    f = False

    if not tagf:
        tag = Tag.objects.get(slug__iexact=slug)
        l = len(Question.objects.filter(tags=tag.id))
        tag_questions = Question.objects.filter(tags=tag.id)
    else:
        l = len(Question.objects.all())
        tag = ''
        tag_questions = Question.objects.all()

    if chpart == 'others':
        available_questions = tag_questions.exclude(part=1).exclude(part=2)
    elif chpart == '1' or chpart == '2':
        available_questions = tag_questions.filter(part=chpart)
    else:
        available_questions = tag_questions

    if chstage == 'ot':
        available_questions = available_questions.exclude(stage='МЭ').exclude(stage='РЭ').exclude(stage='ЗЭ')
    elif chstage == 'МЭ' or chstage == 'РЭ' or chstage == 'ЗЭ':
        available_questions = available_questions.filter(stage=chstage)


    solved_id = Solved.objects.filter(profile=request.user.profile).values()


    while True:
        if k > l:
            f = True
            label = False
            if not tagf:
                label = True
            return render(request, 'main/check.html', {'f': f, 'next': next, 'label': label, 'tag': tag, 'stage': chstage, 'part': chpart})
        if not tagf:
            question_set = available_questions.order_by('-id')[i:k]
        else:
            question_set = available_questions.order_by('-id')[i:k]
        question_dict = question_set.values()

        if question_dict:
            id = question_dict[0]['id']
        else:
            break

        solved_id_list = []
        for el in solved_id:
            solved_id_list.append(el['question_id'])

        if id in solved_id_list:
            i += 1
            k += 1
            continue
        else:
            break

    answer = request.GET.get('answer', '')
    answer1 = str(request.GET.get('answer1', ''))
    answer2 = str(request.GET.get('answer2', ''))
    answer3 = str(request.GET.get('answer3', ''))
    answer4 = str(request.GET.get('answer4', ''))
    answer5 = str(request.GET.get('answer5', ''))
    if not answer:
        answer = str(answer1 + answer2 + answer3 + answer4 + answer5)
    if answer:
        if not tagf:
            label_next = True
        else:
            label_next = False
        question_set = available_questions.order_by('-id')[i:k]
        question_dict = question_set.values()

        question_solved = Solved()
        question_solved.question_id = id
        question_solved.profile = Profile.objects.get(user=request.user)


        right_answer = str(question_dict[0]['answer'])
        next = True
        user_answer = str(answer)
        part = Question.objects.get(id=id).part
        stage = Question.objects.get(id=id).stage
        year = Question.objects.get(id=id).year

        if stage == 'ЗЭ' or stage == 'РЭ' or stage == 'МЭ':
            vseros = True
        else:
            vseros = False


        if part == 3 and vseros:
            for el in international_part3:
                if el[0] == str(stage) and el[1] == str(year):
                    auto2 = True

        if (part == 1 and vseros) or auto1:
            part1f = True
            if user_answer == right_answer:
                result = 'Верно!'
                color = 'limegreen'
                context = {'questions': question_set,
                           'result': result,
                           'color': color,
                           'right_answer': '',
                           'user_answer': user_answer,
                           'next': next,
                           'part1': part1f,
                           'part2': part2f,
                           'partn': partnf,
                           'f': f,
                           'tag': tag,
                           'label_next': label_next,
                           'vseros': vseros, 'auto1': auto1, 'auto2': auto2,
                           'chpart': chpart, 'stage': chstage
                           }

                question_solved.max_score = 1
                question_solved.user_score = 1
                question_solved.user_answer = user_answer
                question_solved.save()

                return render(request, 'main/check.html', context)
            else:
                result = 'Ошибка :('
                color = 'red'
                right = ' Правильный ответ: ' + right_answer + '.'
                context = {'questions': question_set,
                           'result': result,
                           'color': color,
                           'right_answer': right,
                           'user_answer': user_answer,
                           'next': next,
                           'part1': part1f,
                           'part2': part2f,
                           'partn': partnf,
                           'f': f,
                           'tag': tag,
                           'label_next': label_next,
                           'vseros': vseros, 'auto1': auto1, 'auto2': auto2,
                           'chpart': chpart, 'stage': chstage
                           }

                question_solved.max_score = 1
                question_solved.user_score = 0
                question_solved.user_answer = user_answer
                question_solved.save()

                return render(request, 'main/check.html', context)
        elif (part == 2 and vseros) or auto2:
            part2f = True
            norm_score, progr_score, bin_result = counter.counter2(user_answer, right_answer)
            question_solved.max_score = 2.5
            question_solved.user_score = norm_score
            question_solved.user_answer = user_answer
            question_solved.save()

            if norm_score == 2.5:
                result = 'Верно!'
                color = 'limegreen'
            if norm_score == 0 or norm_score == 0.5:
                result = 'Совсем мало правильных ответов :( Ботайте, и всё обязательно получится!'
                color = 'red'
                right = ' Правильный ответ: ' + right_answer + '.' + ' Балл: ' + str(norm_score) + ' (прогрессивная шкала: ' + str(progr_score) + ').'
            if norm_score > 0.5 and norm_score < 2.5:
                result = 'Частично верно. Есть куда стремится :)'
                color = 'darkorange'
                right = ' Правильный ответ: ' + right_answer + '.' + ' Балл: ' + str(norm_score) + ' (ррогрессивная шкала: ' + str(progr_score) + ').'
            context = {'questions': question_set,
                       'result': result,
                       'color': color,
                       'right_answer': '',
                       'user_answer': user_answer,
                       'next': next,
                       'part1': part1f,
                       'part2': part2f,
                       'partn': partnf,
                       'f': f,
                       'right_answer': right,
                       'tag': tag,
                       'label_next': label_next,
                       'vseros': vseros, 'auto1': auto1, 'auto2': auto2,
                       'chpart': chpart, 'stage': chstage
                       }
            return render(request, 'main/check.html', context)

        elif vseros:

            right_list = str(right_answer).split()
            user_list = str(user_answer).split()
            stupid_max = len(right_list)

            stupid_sum = 0
            result_list = []
            for el in user_list:
                result_list.append([el, 'red'])

            for i in range (stupid_max):
                if i > len(user_list) - 1:
                    break
                else:
                    user_str = user_list[i]
                    right_str = right_list[i]

                    if user_str == right_str:
                        stupid_sum += 1
                        result_list[i][1] = 'limegreen'

            partnf = True
            result = 'Проверьте себя.'
            color = 'green'
            right = right_answer
            context = {'questions': question_set,
                           'result': result,
                           'color': color,
                           'right_answer': right,
                           'user_answer': user_answer,
                           'next': next,
                           'part1': part1f,
                           'part2': part2f,
                           'partn': partnf,
                           'f': f,
                           'tag': tag,
                            'right_answer_label': right_answer,
                            'label_next': label_next,
                            'vseros': vseros, 'auto1': auto1, 'auto2': auto2,
                            'stupid_max': stupid_max,
                            'stupid_sum': stupid_sum,
                            'result_list': result_list,
                            'right_list': right_list,
                            'chpart': chpart, 'stage': chstage
                           }
            question_solved.max_score = 0
            question_solved.user_score = 0
            question_solved.user_answer = user_answer
            question_solved.save()

            return render(request, 'main/check.html', context)



        else:
            partnf = True
            result = 'Проверьте себя.'
            color = 'black'
            right = ' Правильный ответ:'
            context = {'questions': question_set,
                           'result': result,
                           'color': color,
                           'right_answer': right,
                           'user_answer': user_answer,
                           'next': next,
                           'part1': part1f,
                           'part2': part2f,
                           'partn': partnf,
                           'f': f,
                           'tag': tag,
                            'right_answer_label': right_answer,
                            'label_next': label_next,
                            'vseros': vseros, 'auto1': auto1, 'auto2': auto2,
                            'chpart': chpart, 'stage': chstage
                           }
            question_solved.max_score = 0
            question_solved.user_score = 0
            question_solved.user_answer = user_answer
            question_solved.save()

            return render(request, 'main/check.html', context)

    question_set = available_questions.order_by('-id')[i:k]
    question_dict = question_set.values()


    id = 0
    part1f = False
    part2f = False
    partnf = False

    if not question_dict:
        f = True
        label = True

    if question_dict:

        f = False
        label = False


        id = question_dict[0]['id']

        part = Question.objects.get(id=id).part
        stage = Question.objects.get(id=id).stage
        year = Question.objects.get(id=id).year

        if stage == 'ЗЭ' or stage == 'РЭ' or stage == 'МЭ':
            vseros = True
        else:
            vseros = False

        if (part == 1 and vseros) or auto1:
            part1f = True
        elif (part == 2 and vseros) or auto2:
            part2f = True
        else:
            partnf = True

        if part == 3:
            for el in international_part3:
                if el[0] == str(stage) and el[1] == str(year):
                    auto2 = True
    return  render(request, 'main/check.html', {'f': f, 'next': next, 'part1': part1f, 'part2': part2f, 'partn': partnf, 'questions': question_set, 'tag': tag, 'auto1': auto1, 'auto2': auto2, 'chpart': chpart, 'label': label, 'stage': chstage})

def personal(request):
    search = request.GET.get('search', '')
    if search:
        return test(request)
    if not request.user.is_authenticated:
        return redirect('login')
    profile = request.user
    prof = Profile.objects.filter(user=profile)
    solved = Solved.objects.filter(profile=prof[0]).values()
    questions = []
    n = 0
    n1 = 0
    n2 = 0
    s1 = 0
    s2 = 0

    tags = Tag.objects.all()
    tstat = {}
    for el in tags:
        tstat[el.name] = [0, 0]
    print(tstat)

    actual_list = list(Question.objects.all())
    actual_id_list = []
    for el in actual_list:
        actual_id_list.append(el.id)


    for el in solved:
        n += 1
        q_id = el['question_id']
        question_list = []
        if q_id in actual_id_list:
            question = Question.objects.get(id=q_id)
        else:
            continue
        questions.append([question, el])

        max_score = el['max_score']
        user_score = el['user_score']

        tag = list(question.tags.values())
        for x in tag:
            tag_name = x['name']
            tstat[tag_name][0] += user_score
            tstat[tag_name][1] += max_score

        if question.part  == 1:
            n1 += 1
            s1 += el['user_score']
        if question.part == 2:
            n2 += 1
            s2 += el['user_score']



    m1 = n1
    m2 = n2 * 2.5
    if m1 == 0:
        p1 = 'неизвестно'
    else:
        p1 = str(int(s1 / m1 * 100)) + ' %'
    if m2 == 0:
        p2 = 'неизвестно'
    else:
        p2 = str(int(s2/m2*100)) + ' %'
    st_list = [n, n1, n2, s1, s2, m1, m2, p1, p2]
    names_list = ['n', 'n1', 'n2', 's1', 's2', 'm1', 'm2', 'p1', 'p2']
    statistics = {}
    for i in range(len(st_list)):
        statistics[names_list[i]] = str(st_list[i])

    tags_list = list(tags)
    tags_list_stat = []
    for i in range(len(tags_list)):
        name = tags_list[i].name
        tags_list_stat.append([tags_list[i], tstat[name]])
    print(tags_list_stat)
    tags_list_percents = []
    for el in tags_list_stat:
        a = el[1][0]
        b = el[1][1]
        if b == 0:
            p = 'неизвестно'
        else:
            p = str(int(a / b * 100)) + ' %'
        tags_list_percents.append([el[0], p])

    show_solved = questions[::-1]

    paginator = Paginator(show_solved, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    chpart = request.GET.get('part', 'n')
    chstage = request.GET.get('stage', 'all')

    return render(request, 'main/personal.html', {'profile': profile,
                                                  'questions': questions,
                                                  'tags': tags_list_percents,
                                                  'st': statistics,
                                                  'show_solved': page,
                                                  'is_paginated': is_paginated,
                                                  'next_url': next_url,
                                                  'prev_url': prev_url,
                                                  'part': chpart,
                                                  'stage': chstage
                                                  })

def dev(request):
    search = request.GET.get('search', '')

    if search:
        return test(request)
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            stage = form.cleaned_data.get("stage")
            year = form.cleaned_data.get("year")
            grade = form.cleaned_data.get("grade")
            part = form.cleaned_data.get("part")
            new_form = QuestionForm(initial={'stage': stage, 'year': year, 'grade': grade, 'part': part} )
            context={'form': new_form}
            return render(request, 'main/dev_cont.html', context)
        else:
            error = 'Во время отправки формы что-то пошло не так :('

    form = QuestionForm()
    context={'form': form}
    return render(request, 'main/dev.html', context)



def test(request):

    search = request.GET.get('search', '')
    lower_search = search.lower()
    upper_search = search.capitalize()
    if search:
        questions = Question.objects.filter(Q(text__icontains=search) |
                                            Q(year__icontains=search) |
                                            Q(grade__icontains=search) |
                                            Q(stage__icontains=search) |
                                            Q(Tag1__name__icontains=search) |
                                            Q(Tag2__name__icontains=search) |
                                            Q(Tag3__name__icontains=search) |
                                            Q(Tag4__name__icontains=search) |
                                            Q(Tag5__name__icontains=search) |
                                            Q(Tag6__name__icontains=search) |
                                            Q(Tag7__name__icontains=search) |
                                            Q(Tag8__name__icontains=search) |
                                            Q(Tag9__name__icontains=search) |
                                            Q(Tag10__name__icontains=search) |
                                            Q(Tag11__name__icontains=search) |
                                            Q(tags__name__icontains=search) |
                                            Q(text__icontains=upper_search) |
                                            Q(year__icontains=upper_search) |
                                            Q(grade__icontains=upper_search) |
                                            Q(stage__icontains=upper_search) |
                                            Q(Tag1__name__icontains=upper_search) |
                                            Q(Tag2__name__icontains=upper_search) |
                                            Q(Tag3__name__icontains=upper_search) |
                                            Q(Tag4__name__icontains=upper_search) |
                                            Q(Tag5__name__icontains=upper_search) |
                                            Q(Tag6__name__icontains=upper_search) |
                                            Q(Tag7__name__icontains=upper_search) |
                                            Q(Tag8__name__icontains=upper_search) |
                                            Q(Tag9__name__icontains=upper_search) |
                                            Q(Tag10__name__icontains=upper_search) |
                                            Q(Tag11__name__icontains=upper_search) |
                                            Q(tags__name__icontains=upper_search) |
                                            Q(text__icontains=lower_search) |
                                            Q(year__icontains=lower_search) |
                                            Q(grade__icontains=lower_search) |
                                            Q(stage__icontains=lower_search) |
                                            Q(Tag1__name__icontains=lower_search) |
                                            Q(Tag2__name__icontains=lower_search) |
                                            Q(Tag3__name__icontains=lower_search) |
                                            Q(Tag4__name__icontains=lower_search) |
                                            Q(Tag5__name__icontains=lower_search) |
                                            Q(Tag6__name__icontains=lower_search) |
                                            Q(Tag7__name__icontains=lower_search) |
                                            Q(Tag8__name__icontains=lower_search) |
                                            Q(Tag9__name__icontains=lower_search) |
                                            Q(Tag10__name__icontains=lower_search) |
                                            Q(Tag11__name__icontains=lower_search) |
                                            Q(tags__name__icontains=lower_search))


    else:
        questions = Question.objects.order_by('-id')


    topic = request.GET.get('topic', '')

    #import urllib
    #topic = str(urllib.parse.unquote(topic_url))

    if topic:
        questions = Question.objects.filter(Q(Tag1__name=topic) |
                                            Q(Tag2__name=topic) |
                                            Q(Tag3__name=topic) |
                                            Q(Tag4__name=topic) |
                                            Q(Tag5__name=topic) |
                                            Q(Tag6__name=topic) |
                                            Q(Tag7__name=topic) |
                                            Q(Tag8__name=topic) |
                                            Q(Tag9__name=topic) |
                                            Q(Tag10__name=topic) |
                                            Q(Tag11__name=topic))

    paginator = Paginator(questions, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    tags = Tag.objects.all()

    context = {
        'title': 'Вопросы',
        'questions': page, 'tags': tags,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'search': search,
        'topic': topic
        }

    return render(request, 'main/test.html', context=context)


def tag_detail(request, slug):

    search = request.GET.get('search', '')
    if search:
        return test(request)

    try:
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'main/tag.html', context={'tag': tag})
    except django.core.exceptions.ObjectDoesNotExist:
        pass


def instructions(request):

    search = request.GET.get('search', '')
    if search:
        return test(request)

    questions = Question.objects.order_by('-id')
    lis = set()
    for el in questions:
        a = el.stage
        b = el.year
        c = el.grade
        l = (a, b, c)
        lis.add(l)
    l = list(lis)
    s = ''
    for i in l:
        for el in i:
            s += str(el)
            s += ' '
        s += '\n'

    return render(request, 'main/instructions.html', context={'q': s, 'questions': questions})




from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):

    search = request.GET.get('search', '')
    if search:
        return test(request)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def signin(request):

    search = request.GET.get('search', '')
    if search:
        return test(request)

    if request.method == 'POST':
        form = login(request, request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('personal')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):

    search = request.GET.get('search', '')
    if search:
        return test(request)


    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('personal')
                else:
                    return HttpResponse('Аккаунт не активен')
            else:
                return HttpResponse('Неверное имя пользователя')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})
