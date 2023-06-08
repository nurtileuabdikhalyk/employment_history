from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from .models import *
from .forms import ConsultationForm, SignUpForm, EmploymentForm, LoginForm, AddEmploymentForm, PlaceOfWorkForm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import datetime


def index(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = ConsultationForm()
    news = News.objects.order_by('-data_created')[:3]
    # news = News.objects.order_by('-data_created').values('title', 'description', 'image', 'data_created', 'slug')[:3]
    context = {'title': 'Электронды еңбек кітапшасының ақпараттық жүйесі', 'news': news, 'form': form}
    return render(request, 'mainapp/index.html', context)



def render_pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=employment_history.pdf'
    styles = getSampleStyleSheet()

    styles['Normal'].fontName = 'Times'

    pdfmetrics.registerFont(TTFont('Times', 'times.ttf'))
    doc = SimpleDocTemplate(response)
    styles.add(ParagraphStyle(name='TestStyle',
                              fontName='Times',
                              fontSize=14, alignment=1
                              ))

    styles.add(ParagraphStyle(name='text',
                              fontName='Times',
                              fontSize=8, alignment=0,
                              ))
    styles.add(ParagraphStyle(name='text_data',
                              fontName='Times',
                              fontSize=8, alignment=0,
                              leftIndent=350
                              ))

    try:
        if request.user.is_staff:
            question = Employment.objects.order_by('customer','data_created')
        elif request.user.employee.staff:
            question = Employment.objects.filter(place_of_work=request.user.employee.place_of_work)
        else:
            question = Employment.objects.filter(customer=request.user.customer)
    except:

        question = Employment.objects.filter(customer=request.user.customer).order_by('data_created')


    elements = []
    s = 'Құжат электрондық үкімет порталымен құрылған'
    elements.append(Paragraph(s, style=styles["text"]))
    text_data = 'Алу күні мен уақыты: ' + str(datetime.datetime.now().day) + '-' + str(
        datetime.datetime.now().month) + '-' + str(datetime.datetime.now().year) + ' ' + str(
        datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)
    elements.append(Paragraph(text_data, style=styles["text_data"]))
    img = Image('D:\\Python\\github\\employment_history\\mainapp\\gerb.jpg', width=30, height=30)
    img.hAlign = "CENTER"
    elements.append(img)

    text_kaz = "Жұмыс туралы мәліметтер"
    p = Paragraph(text_kaz, style=styles["TestStyle"])
    elements.append(p)
    elements.append(Spacer(0, 10))

    data = [
        [
            Paragraph('№', styles["Normal"]),
            Paragraph('Қолданушы', styles["Normal"]),
            Paragraph('Жұмысқа тұрған уақыты', styles["Normal"]),
            Paragraph('Жұмыстан шыққан уақыты', styles["Normal"]),
            Paragraph('Жұмыс орын', styles["Normal"]),
            Paragraph('Лауазымы', styles["Normal"]),
            Paragraph('Құжат, датасы', styles["Normal"]),
        ],
    ]
    count = 1
    for q in question:
        data.append(
            [
                count,
                Paragraph(f"{q.customer.first_name} {q.customer.last_name} {q.customer.fatherland}", styles["Normal"]),
                q.data_created, q.data_ended,
                Paragraph(q.place_of_work.name, styles["Normal"]),
                Paragraph(q.position, styles["Normal"]),
                Paragraph(q.command, styles["Normal"]),
            ])
        count += 1
    t = Table(data)

    t.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.black),
    ]))
    elements.append(t)
    doc.build(elements)

    return response


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            Customer.objects.create(user=user,
                                    first_name=form.cleaned_data['first_name'],
                                    fatherland=form.cleaned_data['fatherland'],
                                    last_name=form.cleaned_data['last_name'],
                                    jsn=form.cleaned_data['jsn'],
                                    birthday=form.cleaned_data['birthday'],
                                    education=form.cleaned_data['education'],
                                    profession=form.cleaned_data['profession'],
                                    email=form.cleaned_data['email'],
                                    )
            return redirect('home')


    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'account/signup.html', context)


def account_login(request):
    messages = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            try:
                login(request, user)
            except:
                messages = "Логин немесе құпия сөз қате!"
                context = {
                    'title': 'Кіру',
                    'form': form,

                    "messages": messages
                }
                return render(request, 'account/login.html', context)

            return redirect('home')
    else:
        form = LoginForm()

    context = {'title': 'Кіру',
               "messages": messages, 'form': form}
    return render(request, 'account/login.html', context)


def signup_place(request):
    if request.method == 'POST':
        form = PlaceOfWorkForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            PlaceOfWork.objects.create(user=user,
                                       name=form.cleaned_data['name'],
                                       bin=form.cleaned_data['bin'],

                                       )
            return redirect('home')
    else:
        form = PlaceOfWorkForm()
    context = {'title': 'Тіркелу', 'form': form}
    return render(request, 'account/signup_place.html', context)


def employment(request):
    try:
        if request.user.is_staff:
            question = Employment.objects.order_by('customer', 'data_created')
        elif request.user.employee.staff:
            question = Employment.objects.filter(place_of_work=request.user.employee.place_of_work)
        else:
            question = Employment.objects.filter(customer=request.user.customer)
    except:
        question = Employment.objects.filter(customer=request.user.customer).order_by('data_created')
    # question = Employment.objects.filter(customer=request.user.customer)
    context = {
        'title': 'Еңбек кітапша',
        'question': question,
        # 'form': form,
    }
    return render(request, 'mainapp/employment.html', context)


def delete(request, id):
    question = Employment.objects.get(id=id)
    question.delete()
    return redirect('employment')


class EmploymentUpdateView(UpdateView):
    template_name = 'mainapp/update.html'
    model = Employment
    form_class = EmploymentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        try:
            if self.request.user.is_staff:
                place = PlaceOfWork.objects.all()
            elif self.request.user.employee.staff:
                place = PlaceOfWork.objects.filter(id=self.request.user.employee.place_of_work.pk)
        except:
            e = Employment.objects.get(customer=self.request.user.customer)
            place = PlaceOfWork.objects.filter(id=e.place_of_work.pk)
        kwargs.update(
            {
                # 'place': self.request.user.employee.place_of_work.pk}
                'place': place}
        )
        return kwargs




def add_employment(request):
    if request.method == 'POST':
        form = AddEmploymentForm(request.user, request.user.employee.place_of_work.pk, request.user.is_staff,
                                 request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('employment')
    form = AddEmploymentForm(request.user, request.user.employee.place_of_work.pk, request.user.is_staff)
    context = {'form': form}
    return render(request, 'mainapp/update.html', context)


def about(request):
    context = {'title': 'Жүйе туралы', }
    return render(request, 'mainapp/about.html', context)


def news(request):
    news = News.objects.order_by('-data_created')
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Жаңалықтар', 'news': news, 'page_obj': page_obj}
    return render(request, 'mainapp/news.html', context)


def news_detail(request, slug):
    question = get_object_or_404(News, slug=slug)
    context = {'new': question, 'title': question.title}
    return render(request, 'mainapp/news-detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = ConsultationForm()
    context = {'title': 'Контактілер', 'form': form}
    return render(request, 'mainapp/contact.html', context)
