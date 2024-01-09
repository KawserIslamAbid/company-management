from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def profile(request):
    return render(request,'profile.html')

def dashboard(request):
    return render(request,'dashboard.html')


def sign_in(request):
    # if request.method == "POST":
    #     user_name = request.POST.get('username')
    #     mail = request.POST.get('email')
    #     pass_word = request.POST.get('password')
    #     usertype = request.POST.get('user_type')
    #     default_profile_pic_url = ('img/default_profile_pic.png')  

    #     user = Custom_User.objects.create_user(username=user_name, password=pass_word)
    #     user.display_name = displayname
    #     user.email = mail
    #     user.user_type = usertype
    #     user.profile_pic = default_profile_pic_url  
    #     user.save()

       
    #     if usertype == 'Admin/HR':
    #         Admin_Profile.objects.create(user=user)
    #     elif usertype == 'System Engineer':
    #         System_Engineer_Profile.objects.create(user=user)
    #     elif usertype == 'Project Manager':
    #         Project_Manager_Profile.objects.create(user=user)
    #     elif usertype == 'Backend Developer':
    #         Backend_Developer_Profile.objects.create(user=user)
    #     elif usertype == 'Ui/Ux Designer':
    #         Ui_Ux_Designer_Profile.objects.create(user=user)
    #     elif usertype == 'Staff':
    #         Staff_Profile.objects.create(user=user)
    #     elif usertype == 'Finance Officer':
    #         Finance_Officer_Profile.objects.create(user=user)

    #     messages.success(request, "Account created successfully.")
    #     return redirect("login")
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')

def forget_pass(request):
    return render(request,'forget_pass.html')

def otp_veify(request):
    return render(request,'otp_veify.html')

def settings(request):
    return render(request,'settings.html')

def eror(request):
    return render(request,'404_eror.html')