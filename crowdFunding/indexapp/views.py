from django.shortcuts import render, get_object_or_404
from projectsapp.models import Project, ProjectRating, Category
from users.models import CustomUser
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Q
from django.db import connection

User = get_user_model()


# Create your views here.
# def index(r):
#     # Get New Projects
#     projects = Project.objects.all().order_by('-id')[:5]
#     projects_top = Project.objects.all().order_by('-rate')[:5]
#     projects_selected = Project.objects.all().order_by('-selected_at_by_admin')[:5]

#     for project in projects:
#         try:
#             rating = ProjectRating.objects.get(ProjectId=project, owner_id=r.user)
#             project.user_rating = rating.rating if rating else 0
#         except:
#             project.user_rating = 0
#     context = {
#         'projects': projects,
#         'projects_top': projects_top,
#         'projects_selected': projects_selected
#     }
#     return render(r, "index.html", context)

def index(r):
    search_post = r.GET.get('search')
    if search_post:
        projects = Project.objects.filter(Q(title__icontains=search_post) | Q(details__icontains=search_post))
        print(projects)
        if projects:
            context = {
                'projects': projects,
            }
            return render(r, "search.html", context)
        else:
            return render(r, "nosearch.html")

    else:
        projects = Project.objects.all().order_by('-id')[:5]
        projects_top = Project.objects.all().order_by('-rate')[:5]
        projects_selected = Project.objects.all().order_by('-selected_at_by_admin')[:5]
        # If not searched, return default posts
        for project in projects:
            try:
                rating = ProjectRating.objects.get(ProjectId=project, owner_id=r.user)
                project.user_rating = rating.rating if rating else 0
            except:
                project.user_rating = 0
        context = {
            'projects': projects,
            'projects_top': projects_top,
            'projects_selected': projects_selected,
        }
        context['categories'] = category_list(r)

    return render(r, "index.html", context)


@login_required
def rate(r, project_id: int, rating: int):
    # userid = r.session['userId']
    # userid = 3
    project = Project.objects.get(id=project_id)
    # user = CustomUser.objects.get(id=userid)
    ProjectRating.objects.filter(ProjectId=project, owner_id=r.user).delete()
    ProjectRating.objects.create(ProjectId=project, owner_id=r.user, rating=rating)
    project.rate = project.average_rating()
    project.save()
    return index(r)


@login_required
def user_profile(request):
    user = request.user
    projects = Project.objects.filter(owner_id=user)
    ratings = ProjectRating.objects.filter(owner_id=user)
    context = {
        'user': user,
        'projects': projects,
        'ratings': ratings
    }
    return render(request, 'user_profile.html', context)


@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.mobile = request.POST['mobile']
        try:
            user.birthday = request.POST['birthday']
        except ValidationError:
            messages.error(request, 'Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return redirect('edit_user_profile')
        user.country = request.POST['country']
        user.facebook_profile = request.POST['facebook_profile']
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('user_profile')
    else:
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'edit_user_profile.html', context)


@login_required
def delete_user_profile(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')
        if user.check_password(password):
            user.delete()
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('/')
        else:
            messages.error(request, 'Wrong password. Please try again.')
            return redirect('delete_user_profile')
    else:
        return render(request, 'delete_user_profile.html')


@login_required
def delete_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id, owner_id=request.user.id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found.')
        return redirect('index')

    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM public.projectsapp_project WHERE id = %s ', [project_id])

    messages.success(request, 'The project has been deleted successfully.')
    return redirect('user_profile')


def category_list(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT public.projectsapp_category.id, projectsapp_category.name, count(projectsapp_project.id) as project_count 
                      FROM projectsapp_category 
                       LEFT OUTER JOIN projectsapp_project ON projectsapp_category.id = projectsapp_project.category_id_id
                       GROUP BY projectsapp_category.id''')
    categories = cursor.fetchall()
    cursor.close()

    context = {'categories': []}
    for category in categories:
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT id, title, details, rate, total_target, current_donation, start_campaign, end_campaign FROM public.projectsapp_project WHERE category_id_id=%s''',[category[0]])
        projects = cursor.fetchall()

        cursor.close()
        context['categories'].append({
            'id': category[0],
            'name': category[1],
            'project_count': category[2],
            'projects': [{
                'id': project[0],
                'title': project[1],
                'details': project[2],
                'rate': project[3],
                'total_target': project[4],
                'current_donation': project[5],
                'start_campaign': project[6],
                'end_campaign': project[7],

            } for project in projects],
        })

    return context['categories']
    # return render(request, 'category_list.html', context)


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_details.html', {'project': project})


def handler404(request, exception):
    return render(request, '404.html', status=404)
