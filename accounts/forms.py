#UserCreationFormクラスをインポートする
from django.contrib.auth.forms import UserCreationForm

#models.pyで定義したカスタムUserモデルをインポートする
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:

        #連携するUserモデルを設定
        model=CustomUser

        #フォームで使用するフィールドを設定
        #ユーザー名、メールアドレス、パスワード、パスワード（確認用）
        fields=('username','email','password1','password2')
