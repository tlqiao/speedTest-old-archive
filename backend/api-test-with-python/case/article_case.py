import pytest
from api.article import get_article, add_article


@pytest.mark.parametrize("articleTitle", [("demo22233")])
def test_should_add_article_successfully(articleTitle):
    add_article(articleTitle)


def test_should_get_articles_successfully():
    response = get_article()
    assert response.json()["articlesCount"] > 0
