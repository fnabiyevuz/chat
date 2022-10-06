from django.shortcuts import render

def Group(request):

    return render(request, 'group.html')


def Chat(request, group, username):
    if request.method == "POST":
        r = request.POST
        # group = r['group']
        username = r['username']
        context = {
            'group':group,
            'username':username
        }
        return render(request, 'chat.html', context)
    else:
        context = {
            'group': group,
            'username':username
        }
        return render(request, 'chat.html', context)



def Direct(request, group, username):
    if request.method == "POST":
        r = request.POST
        # group = r['group']
        username = r['username']
        context = {
            'group':group,
            'username':username
        }
        return render(request, 'chat.html', context)
    else:
        print(group)
        print(username)
        context = {
            'group': group,
            'username': username,
        }
        return render(request, 'direct.html', context)