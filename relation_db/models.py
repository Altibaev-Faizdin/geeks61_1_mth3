from django.db import models


#Many-to-Many (Машина может иметь много тегов, и один тег может быть у многих машин)
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class NumberCar(models.Model):
    name_car = models.CharField(
        max_length=100,
        default='Lexus 570'
    )
    number_car = models.CharField(
        max_length=20,
        default='....KG....'
    )
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return f"{self.name_car}-------------{','.join(i.name for i in self.tags.all())}"


# One-to-One (1 машина — 1 документ)
class DocumentCar(models.Model):
    choice_car = models.OneToOneField(
        NumberCar,
        on_delete=models.CASCADE,
        related_name='car'
    )
    document = models.CharField(max_length=100)

    def __str__(self):
        return f"Документ: {self.document} ({self.choice_car})"


# One-to-Many (1 машина — много отзывов)
class Review(models.Model):
    MARKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    choice_car = models.ForeignKey(
        NumberCar,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    marks = models.CharField(
        max_length=1,
        choices=MARKS,
        default='5'
    )
    text = models.CharField(
        max_length=255,
        default='good car'
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.choice_car} | {self.marks} | {self.text}"