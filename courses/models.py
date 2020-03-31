from django.db import models


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    #one-to-many or many-to-one relationship
    #a course can have many steps but a step can only belone to one course

    class Meta:
        #allows for ordering in admin
        ordering = ['order',]

    def __str__(self):
        return self.title

