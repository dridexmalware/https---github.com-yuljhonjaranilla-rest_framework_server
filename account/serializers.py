from djoser.serializers import UserCreateSerializer
from account.models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User,
        fields=('id', 'first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')