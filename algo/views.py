from django.shortcuts import render
from .qm2 import mains


# Create your views here.
def home(request):
    x = solve(request)
    return render(request, 'home copy.html',x)

def solve(request):
    minterm = request.GET.get('minterms')
    if minterm:
        d = {}
        d['status']= True
        dc = request.GET.get('dontcare')
        first_group,second_group,third_group,all_prime,prime_header,final_min,prime_t,essential,solu = mains(minterm,dc)
        d['first_group'] = first_group
        d['second_group'] = second_group
        d['third_group'] = third_group
        d['all_prime'] = all_prime
        d['prime_header'] = prime_header
        d['final_min'] = final_min
        d['prime_t'] = prime_t
        d['essential'] = essential
        d['solu'] = solu
        print(d)
        return d
    else:
        return {'status': False}
    
#main("1 2 3","2 4")