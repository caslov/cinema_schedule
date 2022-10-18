import pytest
# from django.contrib.auth.models import User


@pytest.mark.ClassProject
def test_my_user():
    me = User.objects.get(username='admin')
    assert me.is_superuser