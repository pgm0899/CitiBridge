from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from TakeInput.ClearFeedBackendCode import ClearFeed


def take_input_view(request):
    return render(request, "take_input_page.html", {})


def submit1_view(request):
    if request.method == "POST":
        myFileUpload = request.FILES['myFileUpload']  # get the uploaded file

        # store file in TakeInput/Files/upload1.txt
        print(myFileUpload)
        with open('static/upload.txt', 'wb+') as destination:
            for chunk in myFileUpload.chunks():
                destination.write(chunk)

        # call the function and store output
        cf = ClearFeed()
        cf.validate()

        # and return the result
        return render(request, "display_output_page.html", {})
    else:
        return render(request, "take_input_page.html", {})


def submit2_view(request):
    if request.method == "POST":
        transRef = request.POST['transRef']
        valueDate = request.POST['valueDate']
        payerName = request.POST['payerName']
        payerAccNo = request.POST['payerAccNo']
        payeeName = request.POST['payeeName']
        payeeAccNo = request.POST['payeeAccNo']
        amount = request.POST['amount']

        str1 = transRef + valueDate + payerName + ' ' + payerAccNo + payeeName + ' ' + payeeAccNo + ' ' + amount
        with open('static/upload.txt', 'w') as destination:
            destination.writelines(str1)

        # call the function and store output
        cf = ClearFeed()
        cf.validate()

        # and return the result
        return render(request, "display_output_page.html", {})
    else:
        return render(request, "take_input_page.html", {})
