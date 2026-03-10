from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        { 'name' : 'Rohit Sharma', 'age' : 26},
        { 'name' : 'Hardik', 'age' : 16},
        { 'name' : 'Virat Kohali', 'age' : 32},
        { 'name' : 'Surkumar Yadav', 'age' : 19},
        { 'name' : 'Yuvi', 'age' : 27}
    ]

    text = """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis, corporis excepturi, maxime optio unde corrupti harum explicabo magnam ipsa necessitatibus fugiat nulla voluptates asperiores non pariatur ratione adipisci reiciendis odit, libero tempore quos fugit officia. Consequuntur dicta sit optio laboriosam quos amet quam reiciendis at. Quam sint officiis voluptatum aliquam praesentium, ea consequuntur assumenda aliquid fugit, optio dolorem tempora quis voluptates nulla minus qui porro amet? Laboriosam odio quos minima laborum fuga, harum maxime aut? Voluptate, molestias rerum, temporibus suscipit necessitatibus accusantium laboriosam tenetur et asperiores sapiente omnis, tempora cupiditate vero consequuntur ullam eius recusandae a ad soluta enim magnam!
        """

    return render(request, "index.html", context={'peoples' : peoples, 'text' : text})

def success_page(request):
    print("*" * 10)
    return HttpResponse("This is Success Page !")