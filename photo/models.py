from django.db import models

#accountsアプリのmodelsモジュールからCustomUserをインポートする
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):

    #カテゴリ名のフィールド
    title=models.CharField(
        verbose_name='カテゴリ',  #フィールドのタイトル
        max_length=20)

    def __str__(self):

        return self.title


class PhotoPost(models.Model):


    #CustomUserモデル（のuser_id）とPhotoPostモデルを１対多の関係で結びつける
    #CustomUserが親でPhotoPostが子の関係となる
    user=models.ForeignKey(
        CustomUser,

        #フィールドのタイトル
        verbose_name='ユーザー',

        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )

    #Categoryモデル（のtitle）とPhotoPostモデルを１対多の関係で結びつける
    #Categoryが親でPhotoPostが子の関係となる
    category=models.ForeignKey(
        Category,

        #フィールドのタイトル
        verbose_name='カテゴリ',

        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.PROTECT
        )

    #タイトル用のフィールド
    title=models.CharField(
        verbose_name='タイトル',  #フィールドのタイトル
        max_length=200           #最大文字数は200
        )
    
    #コメント用のフィールド
    comment=models.TextField(
        verbose_name='コメント',   #フィールドのタイトル
        )

    #イメージのフィールド１
    image1=models.ImageField(
        verbose_name='イメージ１',  #フィールドのタイトル
        upload_to='photos'         #MEDIA_ROOT以下のphotosにファイルを保存
        )

    #イメージのフィールド２
    image2=models.ImageField(
        verbose_name='イメージ２', #フィールドのタイトル
        upload_to='photos',        #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,               #フィールド値の設定は必須でない
        null=True                 #データベースにnullが保存されることを許容
        )

    #投稿日時のフィールド
    posted_at=models.DateTimeField(
        verbose_name='投稿日時',    #フィールドのタイトル
        auto_now_add=True         #日時を自動追加
        )

    def __str__(self):

        # Returns(str):投稿記事のタイトル
        return self.title

