from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})

def addition(request):
    from random import randint
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        if not answer:
            color = "warning"
            my_ans = "You forgot to enter answer!!"
            return render(request, 'website/division.html', {'my_ans': my_ans,
                                                             'num_1': num_1,
                                                             'num_2': num_2,
                                                             'color': color})
        correct_ans = int(old_num_1)+int(old_num_2)

        if int(answer)==correct_ans:
            my_ans = "Correct " + old_num_1  +" + "+ old_num_2 +" = " +answer
            color = "success"
            # print("Your answer is correct ")
        else:
            my_ans = "Incorrect " + old_num_1  +" + "+ old_num_2 +" is not " +answer + " it is " +str(correct_ans)
            color = "danger"
            # print("Wrong answer.. Correct answer is {correct_ans}" )
        return render(request,'website/addition.html',{'answer':answer,
                                                       'my_ans': my_ans,
                                                       'num_1': num_1,
                                                       'num_2': num_2,
                                                       'color': color})

    return render(request, 'website/addition.html', {'num_1':num_1, 'num_2':num_2})


def subtraction(request):
    from random import randint
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        if not answer:
            color = "warning"
            my_ans = "You forgot to enter answer!!"
            return render(request, 'website/division.html', {'my_ans': my_ans,
                                                             'num_1': num_1,
                                                             'num_2': num_2,
                                                             'color': color})
        correct_ans = int(old_num_1)-int(old_num_2)

        if int(answer)==correct_ans:
            my_ans = "Correct " + old_num_1  +" - "+ old_num_2 +" = " +answer
            color = "success"
            # print("Your answer is correct ")
        else:
            my_ans = "Incorrect " + old_num_1  +" - "+ old_num_2 +" is not " +answer + " it is " +str(correct_ans)
            color = "danger"
            # print("Wrong answer.. Correct answer is {correct_ans}" )
        return render(request,'website/subtraction.html',{'answer':answer,
                                                       'my_ans': my_ans,
                                                       'num_1': num_1,
                                                       'num_2': num_2,
                                                       'color': color})
    return render(request, 'website/subtraction.html', {'num_1':num_1, 'num_2':num_2})

def multiplications(request):
    from random import randint
    num_1 = randint(0,10)
    num_2 = randint(0,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        if not answer:
            color = "warning"
            my_ans = "You forgot to enter answer!!"
            return render(request, 'website/division.html', {'my_ans': my_ans,
                                                             'num_1': num_1,
                                                             'num_2': num_2,
                                                             'color': color})
        correct_ans = int(old_num_1)*int(old_num_2)

        if int(answer)==correct_ans:
            my_ans = "Correct " + old_num_1  +" x "+ old_num_2 +" = " +answer
            color = "success"
            # print("Your answer is correct ")
        else:
            my_ans = "Incorrect " + old_num_1  +" x "+ old_num_2 +" is not " +answer + " it is " +str(correct_ans)
            color = "danger"
            # print("Wrong answer.. Correct answer is {correct_ans}" )
        return render(request,'website/multiplications.html',{'answer':answer,
                                                       'my_ans': my_ans,
                                                       'num_1': num_1,
                                                       'num_2': num_2,
                                                       'color': color})
    return render(request, 'website/multiplications.html', {'num_1':num_1, 'num_2':num_2})

def division(request):
    from random import randint
    num_1 = randint(0,10)
    num_2 = randint(1,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        if not answer:
            color = "warning"
            my_ans = "You forgot to enter answer!!"
            return render(request, 'website/division.html', {'my_ans': my_ans,
                                                             'num_1': num_1,
                                                             'num_2': num_2,
                                                             'color': color})

        correct_ans = int(old_num_1)/int(old_num_2)

        if float(answer)==correct_ans:
            my_ans = "Correct " + old_num_1  +" / "+ old_num_2 +" = " +answer
            color = "success"
            # print("Your answer is correct ")
        else:
            my_ans = "Incorrect " + old_num_1  +" / "+ old_num_2 +" is not " +answer + " it is " +str(correct_ans)
            color = "danger"
            # print("Wrong answer.. Correct answer is {correct_ans}" )
        return render(request,'website/division.html',{'answer':answer,
                                                       'my_ans': my_ans,
                                                       'num_1': num_1,
                                                       'num_2': num_2,
                                                       'color': color})
    return render(request, 'website/division.html', {'num_1':num_1, 'num_2':num_2})

