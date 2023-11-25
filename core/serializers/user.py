from rest_framework.serializers import ModelSerializer, SlugRelatedField    

from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import User


class UserSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = User
        fields = "__all__"
class UserDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)