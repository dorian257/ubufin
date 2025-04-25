from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page   


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)  # Log the user out after password change
            messages.success(request, "Votre mot de passe a été modifié avec succès. Veuillez vous reconnecter.")
            return redirect('login')  # Redirect to the login page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form})
