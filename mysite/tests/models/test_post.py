#test_post.py este arquivo de teste utiliza pytest e pytest-django para testar a criação de um post publicado usando uma factory.

import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'