from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework import generics, permissions

from .models import Contact
from .serializers import ContactSerializer


def contact_page(request):
    errors = {}
    if request.method == "POST":
        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Thanks for reaching out. I will reply soon.")
            return redirect("contact")
        errors = serializer.errors
        messages.error(request, "Please check the form and try again.")
    return render(request, "contact.html", {"errors": errors, "form_data": request.POST})


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
