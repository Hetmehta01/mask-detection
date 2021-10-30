from django.shortcuts import render, redirect
import cv2

def mainpage(request):

    return render(request, 'index.html')

def camera(request):
    if request.method == 'POST':

        cam = cv2.VideoCapture(0)

        image = cam.read()[1]

        cv2.imshow("image", image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


from django.shortcuts import render

# Create your views here.
