from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ MOSDAC AI Help Bot is running!")

from rest_framework.decorators import api_view
from django.http import JsonResponse
from .qa_engine import get_answer_from_docs

@api_view(["POST"])
def ask_question(request):
    question = request.data.get("question", "")
    if not question:
        return JsonResponse({"answer": "Please ask a valid question."})

    answer = get_answer_from_docs(question)
    return JsonResponse({"answer": answer})
