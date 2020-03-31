from django.test import TestCase
from django.utils import timezone
from .models import Course, Step
from django.urls import reverse #tests a url name exist

#Testing course models
class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title = "Python testing",
            description = "Learning python testing models"
        )
        now = timezone.now()
        self.assertLess(
            course.created_at, now
        )

#Testing Step Model
class StepModelTests(TestCase):
    def test_step_creation(self):
        step = Step.objects.create(
            title = "Step testing",
            description = "Testing steps models",
            content = "This is about testing steps",
            order=0,
            course = Course.objects.create(
            title = "Python testing",
            description = "Learning python testing models"
        ))
        step.save()
        #self.assertEqual(step.title, "Step testing") Passed!
        self.assertEqual(step.course.title, "Python testing") #Passed!


"""
class WriterModelTestCase(TestCase):
    def test_instance_creation(self):
        writer = Writer.objects.create(name="humphrey", email="hbutau@msn.com", bio="warup")
        self.assertIn(writer.email, writer.mailto())

"""
#Creating test instances
class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title = 'Python Testing',
            description = 'Learn to write tests in Python'
        )
        self.course2 = Course.objects.create(
            title = 'New Course',
            description = 'A new course'
        )
        self.step = Step.objects.create(
            title = "Introduction to Doctests",
            description = "Learn to write tests in your docstring",
            course = self.course
        )

    #Testing course_list views.py, urls.py and template        
    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:course_list')) #test the response of the url at courses/course_list
        self.assertEqual(resp.status_code, 200) #test if the url at course_list works
        self.assertIn(self.course, resp.context['courses']) #test if instance course created at self.course has two keys: title, and description plus values
        self.assertIn(self.course2, resp.context['courses']) #test if instance course2 created at self.course2 has two keys title, and description plus values
        self.assertTemplateUsed(resp, 'courses/course_list.html') #Tests the template
        self.assertContains(resp, self.course.title) #Tests if the response has a course title


    #Testing course_detail views.py, urls.py and template        
    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={'pk': self.course.pk})) #used to passed in key and value for the pk
        self.assertEqual(resp.status_code, 200) #test if the url at course_list works
        self.assertTrue(self.course.title, 'Python Testing')
        self.assertTrue(self.course2.description, 'A new course')
        self.assertEqual(self.course, resp.context['course'])
        self.assertTemplateUsed(resp, 'courses/course_detail.html')
        self.assertContains(resp, self.course.description)


    #Testing step_detail views.py, urls.py and template        
    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={'course_pk': self.course.pk, 'step_pk': self.step.pk})) #kwargs info comes from courses/course_detail.html
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(self.step.course.title, 'Introduction to Doctests')
        self.assertTrue(self.step.course.description, 'Learn to write tests in your docstring')
        self.assertEqual(self.step, resp.context['step'])
        self.assertTemplateUsed(resp, 'courses/step_detail.html')
        self.assertContains(resp, self.step.course.title)

