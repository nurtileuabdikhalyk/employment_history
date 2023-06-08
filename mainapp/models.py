from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField("Аты", max_length=255, )
    last_name = models.CharField('Тегі', max_length=255, )
    email = models.EmailField("Почта", max_length=255, null=True)
    place_of_work = models.ForeignKey('PlaceOfWork', verbose_name='Жұмыс орын', on_delete=models.CASCADE, blank=True,
                                      null=True)
    staff = models.BooleanField('Қызметкер', default=False)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    class Meta:
        db_table = 'employees'
        verbose_name = "Қызметкер"
        verbose_name_plural = "Қызметкерлер"


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField('Аты', max_length=255, null=True, blank=True)
    fatherland = models.CharField('Әкесінің аты', max_length=255, null=True, blank=True)
    last_name = models.CharField('Тегі', max_length=255, null=True, blank=True)
    email = models.CharField('Почта', max_length=255, null=True, blank=True)
    jsn = models.CharField("ЖСН", max_length=12, null=True, blank=True)
    birthday = models.DateField("Туылған күні", null=True, blank=True)
    education = models.CharField("Білімі", max_length=255, null=True, blank=True)
    profession = models.CharField('Кәсіби мамандығы', max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.fatherland}"

    class Meta:
        db_table = 'customers'
        verbose_name = "Қолданушы"
        verbose_name_plural = "Қолданушылар"


class PlaceOfWork(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Мекеме аты', max_length=255)
    bin = models.CharField('БСН', max_length=12)
    created = models.DateTimeField('Тіркелу уақыты', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'placeofworks'
        verbose_name = "Жұмыс орын"
        verbose_name_plural = "Жұмыс орындар"


class Employment(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Қолданушы', on_delete=models.CASCADE)

    place_of_work = models.ForeignKey(PlaceOfWork, verbose_name='Жұмыс орын', on_delete=models.CASCADE, blank=True,
                                      null=True)
    position = models.CharField("Лауазымы", max_length=255, blank=True, null=True)
    data_created = models.DateField("Жұмысқа тұрған уақыты", blank=True, null=True)
    data_ended = models.DateField("Жұмыстан шыққан уақыты", blank=True, null=True)
    command = models.CharField('Құжат,күні', max_length=255, blank=True, null=True)
    file = models.FileField('Файл', upload_to='files/', null=True, blank=True)

    def get_absolute_url(self):
        return f"/employment/"

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"

    class Meta:
        db_table = 'employments'
        verbose_name = "Еңбек кітапша"
        verbose_name_plural = "Еңбек кітапша"


class Consultation(models.Model):
    name = models.CharField("Аты", max_length=255)
    email = models.EmailField("E-mail")
    message = models.TextField("Хабарлама", max_length=5000)
    completed = models.BooleanField("Орындалды", default=False)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}  {self.email}"

    class Meta:
        db_table = "consultations"
        verbose_name = "Кеңес алушы"
        verbose_name_plural = "Кеңес алушылар"


class News(models.Model):
    title = models.CharField("Тақырыбы", max_length=255)
    description = models.TextField("Сипаттамасы", max_length=5000)
    image = models.ImageField("Сурет", upload_to="news/")
    data_created = models.DateTimeField("Күні", auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "news"
        verbose_name = "Жаңалық"
        verbose_name_plural = "Жаңалықтар"


class Reward(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Қолданушы', on_delete=models.CASCADE)
    place_of_work = models.CharField("Наградтаулар және көтермелеулер", max_length=3000, blank=True, null=True)
    data_created = models.DateField("Күні", blank=True, null=True)
    command = models.CharField('Құжат,датасы', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.customer.first_name} - {self.place_of_work}"

    class Meta:
        db_table = 'rewards'
        verbose_name = "Наградтау және көтермелеу"
        verbose_name_plural = "Наградтаулар және көтермелеулер"
