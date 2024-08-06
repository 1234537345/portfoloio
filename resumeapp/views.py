from django.shortcuts import render,redirect
from .models import resumeprofile

def createprofile(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        universityCollege = request.POST.get('universityCollege')
        DegreeCertification = request.POST.get('DegreeCertification')
        graduation = request.POST.get('graduation')
        skills = request.POST.get('skills')
        projecttitle = request.POST.get('projecttitle')
        projectdescription = request.POST.get('projectdescription')
        coursetitle=request.POST.get('coursetitle')
        prjectimg=request.POST.get('prjectimg')
        prjectlink=request.POST.get('prjectlink')
        p = resumeprofile(
            fullname=fullname,
            phone=phone,
            address=address,
            email=email,
            universityCollege=universityCollege,
            DegreeCertification=DegreeCertification,
            graduation=graduation,
            skills=skills,
            projecttitle=projecttitle,
            projectdescription=projectdescription,
            coursetitle=coursetitle,
            prjectimg=prjectimg,
            prjectlink=prjectlink
        )
        p.save()
    return render(request, 'profile.html')

def listdetails(request):
    values = resumeprofile.objects.all()

    return render(request, 'listdetails.html', {'values': values})






def updatedetails(request, p_id):
    p = resumeprofile.objects.get(id=p_id)
    if request.method == 'POST':

        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        universityCollege = request.POST.get('universityCollege')
        DegreeCertification = request.POST.get('DegreeCertification')
        grduation = request.POST.get('grduation')
        skills = request.POST.get('skills')
        projecttitle = request.POST.get('projecttitle')
        projectdescription = request.POST.get('projectdescription')
        coursetitle=request.POST.get('coursetitle')
        prjectimg=request.POST.get('prjectimg')
        prjectlink=request.POST.get('prjectlink')


        p.fullname = fullname
        p.phone = phone
        p.address = address
        p.email = email
        p.universityCollege = universityCollege
        p.DegreeCertification = DegreeCertification
        p.grduation = grduation
        p.skills = skills
        p.projecttitle = projecttitle
        p.projectdescription = projectdescription
        p.coursetitle=coursetitle
        p.prjectimg=prjectimg
        p.prjectlink=prjectlink
        p.save()
        return redirect('details')
    return render(request, 'updatedetails.html', {'p':p})


def deletedetails(request,p_id):
    p = resumeprofile.objects.get(id=p_id)
    p.delete()
    return redirect('details')




