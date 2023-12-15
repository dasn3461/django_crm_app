from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record


#Login Function
def home(request):
    records=Record.objects.all()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have login succcessfully!!')
            return redirect('home')
        else:
            messages.success(request, "you couldn't find an account with that username.Try another or new account")
            return redirect('home')
        
    else:    
        return render(request, 'home.html', {'records':records})
    return render(request, 'home.html')


# Logout Function
def user_logout(request):
    logout(request)
    messages.success(request, 'you have logout succcessfully!!')
    return redirect('home')

# Registration Function
def Register_User(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        password1=request.POST['password1']
        password2=request.POST['password2']
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup Create successfully')
            return redirect('home')
        
        elif password1!=password2:
            messages.success(request, 'your passswword does not match!!')
            return redirect('register')
            
            
    else:    
        form=SignUpForm()
        return render(request, 'signup.html', {'form':form})
    return render(request, 'signup.html')
    

# Customer Record
def custoer_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You must have to login to see data !!')
        return redirect('home')
    
    
    
# Delete Function
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record=Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'record delete successfully')
        return redirect('home')
    else:
        messages.success(request, 'You must have to login account !!')
        return redirect('home')


# Add Record Function

def add_record(request):
    form=AddRecordForm()
    if request.user.is_authenticated:
        if request.method=="POST":
            form=AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'record add successfully!!')
                return redirect('home')
            else:   
                messages.success(request, 'You must have to login or add record !!')
                return redirect('home') 
        else:    
            return render(request, 'addrecord.html', {'form':form})
        return render(request, 'addrecord.html')
    
    
    
# Update Record Function    
def update_record(request,pk):
    if request.user.is_authenticated:
        if request.method=="POST":
            current_record=Record.objects.get(id=pk)
            form=AddRecordForm(request.POST,instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, 'record update successfully!!')
                return redirect('home')
            
        else:
            current_record=Record.objects.get(id=pk)
            form=AddRecordForm(instance=current_record)
        return render(request, 'update.html', {'form':form})    
                
    
    
    
       
        
    