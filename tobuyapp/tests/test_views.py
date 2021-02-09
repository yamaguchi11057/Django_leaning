from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary

class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        #テストユーザーのパスワード
        self.password = 'testpass'

        #各インスタンスメソッドで使うテスト用ユーザー生成し、インスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
            username='user',
            email='test_mail@test.com',
            password=self.password)
        
        self.client.login(email=self.test_user.email, password=self.password)

class TestDiaryCreateView(LoggedInTestCase):
    """DiaryCreateView用のテストクラス"""

    def test_create_diary_success(self):
        """日記作成処理が成功することを検証する"""

        #Postパラメータ
        params = {
            'title':'テストタイトル',
            'content':'本文',
            'photo1':'',
            'photo2':'',
            'photo3':'',
        }
        #新規日記作成処理(post)を実行
        response = self.client.post(reverse_lazy('tobuyapp:diary_create'), params)

        #日記リストページへのリダイレクト検証
        self.assertRedirects(response, reverse_lazy('tobuyapp:diary_list'))

        #日記データがデータベースに登録されたか検証
        self.assertEqual(Diary.objects.filter(title='テストタイトル').count(), 1)

    def test_create_diary_failure(self):
        """新規日記作成処理が失敗することを検証する"""

        #日記作成処理(POST)を実行
        response = self.client.post(reverse_lazy('tobuyapp:diary_create'))

        #必須フォームフィールドが未入力によりエラーになることを検証する
        self.assertFormError(response, 'form', 'title', 'This field is required.')

class TestDiaryUpdateView(LoggedInTestCase):
    """DiaryUpdateView用テストクラス"""
    def test_update_diary_success(self):
        """日記編集処理が成功することを検証する"""

        #テスト用日記データの作成
        diary = Diary.objects.create(user=self.test_user, title='タイトル編集前')

        #POSTパラメータ
        params = {
            'title':'タイトル編集後'
        }

        #日記編集処理(POST)を実行
        response = self.client.post(reverse_lazy('tobuyapp:diary_update', kwargs={'pk':diary.pk}), params)

        #日記詳細ページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('tobuyapp:diary_detail', kwargs={'pk':diary.pk}))

        #日記データが編集されたか検証
        self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'タイトル編集後')


    def test_update_diary_failure(self):
        """日記編集呂理が失敗することを検証"""

        #日記作成処理の実行
        response = self.client.post(reverse_lazy('tobuyapp:diary_update', kwargs={'pk':999}))

        #存在しない日記データを編集しようとしてエラーがになることを検証
        self.assertEqual(response.status_code, 404)

class TestDiaryDeleteView(LoggedInTestCase):
    """DiaryDeleteView用のテストクラス"""
    #テスト用日記データの作成
    def test_delete_diary_success(self):
        diary = Diary.objects.create(user=self.test_user, title="タイトル")

        #日記削除処理を実行
        response = self.client.post(reverse_lazy('tobuyapp:diary_delete', kwargs={'pk':diary.pk}))

        #日記リストページへリダイレクト
        self.assertRedirects(response, reverse_lazy('tobuyapp:diary_list'))

        #日記データが削除されたか検証
        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

    def test_delete_diary_failure(self):
        """日記削除処理が失敗することを検証"""

        #日記削除処理の実行
        response = self.client.post(reverse_lazy('tobuyapp:diary_delete', kwargs={'pk':999}))

        #存在しない日記データを削除しようとしてエラーになることを検証
        self.assertEqual(response.status_code, 404)