from leancloud import User
from leancloudbb.forum.models import Category

__author__ = 'pan'

def create_test_data(users=5, categories=2, forums=2, topics=1, posts=1):
    # create 5 users
    for u in range(1, users + 1):
        username = "test%s" % u
        email = "test%s@example.org" % u
        user = User()
        user.set("username", username)
        user.set("password", "test")
        user.set("email", email)
        user.sign_up()

    # create 2 categories
    for i in range(1, categories + 1):
        category_title = "Test Category %s" % i
        category = Category(title=category_title,
                            description="Test Description")
        category.save()

        # create 2 forums in each category

    return "create success"
