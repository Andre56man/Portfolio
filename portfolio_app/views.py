from django.shortcuts import render
from .models import Project
from portfolio_app.models import Project
Project.objects.all()


def home(request):
    projects = Project.objects.order_by('-created_at')[:20]
    return render(request, 'portfolio_app/home.html', {'projects': projects})
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, render

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New message from {name}"
        full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            "ton_email@exemple.com",  # expéditeur (paramétré dans settings)
            ["kodjoandre56@example.com"],  # destinataire
            fail_silently=False,
        )

        messages.success(request, "✅ Message sent successfully! Thank you.")
        return redirect("home")
    return redirect("home")
