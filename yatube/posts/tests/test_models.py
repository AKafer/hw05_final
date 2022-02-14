from django.test import TestCase
from ..models import Group, Post, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая группа, здесь больше 15 символов',
        )

    def test_models_have_correct_Str_name(self):
        """Проверяем, что у моделей Post, Group корректно работает __str__."""
        post = PostModelTest.post
        group = PostModelTest.group
        dict_equal = {
            post: post.text[:15],
            group: group.title
        }
        for model, expected_value in dict_equal.items():
            with self.subTest(model=model):
                self.assertEqual(expected_value, str(model))

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        field_verboses = {
            'text': 'Текст',
            'author': 'Автор',
            'group': 'Группа',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    Post._meta.get_field(field).verbose_name, expected_value)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        field_help_texts = {
            'text': 'Текст поста',
            'author': 'Подпишите свой опус',
            'group': 'Опеределите группу',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    Post._meta.get_field(field).help_text, expected_value)
