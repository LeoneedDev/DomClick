from django.test import TestCase

from .models import UserModel,MemberModel


class ModelTest(TestCase):

    def setUp(self) -> None:
        self.user = UserModel.objects.create(
            firstname='testfirstname',
            lastname='testlastname',
            title='open',
            number='9312458742',
            mail='test@test.ru',
            tel_name='teltestname',
            notifications=True,
            profile_id='836952169'
        )

class MemberTest(TestCase):

    def setUp(self) -> None:
        self.user = MemberModel.objects.create(
            username='mabertest',
            firstname='testfirstnamemember',
            lastname='testlastnamemember',
            workmail='test@test-member.ru',
            position='director'
        )
