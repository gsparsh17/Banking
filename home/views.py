from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
# from home.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

OTP = get_random_string(4, allowed_chars='0123456789')
OTP1 = get_random_string(4, allowed_chars='0123456789')



# from .forms import UpdateProfileForm

def index(request):
    
    return render(request, 'index.html')
    # return HttpResponse("This Is Homepage")
def about(request):
    return render(request, 'about.html')
def welcome(request):
    if request.user.is_anonymous:
        return redirect("/index")
    context={
        "name":"User",
        "OTP":OTP
    }

    if request.method == "POST":
        print("hello")
        send_mail(
    "Congratulations!",
    "Your OTP For Bank Of Lucknow Account Is:"+OTP,
    "lucknowbankof4@gmail.com",
    ["2200520310056@ietlucknow.ac.in"],
    fail_silently=False,
)
    return render(request, 'welcome.html', context)
    
def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        User = authenticate(username=username,password=password)
        if User is not None:
            print(User)
            login(request, User)
            send_mail(
    "Logged In!",
    "Welcome "+request.user.first_name+",You Are Successfully Logged In to Your (Bank Of Lucknow) Bank Account.",
    "lucknowbankof4@gmail.com",
    [request.user.email],
    fail_silently=False,
)
            return redirect("/welcome")
        else:
            return render(request, 'index.html')
    return render(request, 'login1.html')
def register(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        city = request.POST.get('city')
        phoneNo = request.POST.get('phoneNo')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        CustID = request.POST.get('CustID')
        password = request.POST.get('password')
        contact=Contact(firstname=firstname, lastname=lastname, username=username, city=city, phoneNo=phoneNo, state=state, pincode=pincode, CustID=CustID, password=password)
        contact.save()
        # profile=Profile(balance='0')
        # profile.save()
        user = User.objects.create_user(username=username, email=CustID, password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        send_mail(
    "Congratulations!",
    "Welcome "+firstname+", Your Details has been successfully registered with us.Your (Bank Of Lucknow) Bank Account has been successfully openned.Your Username (Customer ID) is"+username+" & Your Password is"+password,
    "lucknowbankof4@gmail.com",
    [CustID],
    fail_silently=False,
)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # profile_form.save()
        return redirect("/login1")
    return render(request, 'register.html')

def logout1(request):
    logout(request)
    return redirect("/index")
