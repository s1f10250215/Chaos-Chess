from django.shortcuts import render

# Create your views here.
def index(request):
    """トップページ（モード選択画面）"""
    return render(request, 'game/index.html')