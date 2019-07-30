from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from maps import urls as map_urls
from bizzzzz import urls as business_urls
from accounts import urls as accounts_urls
from s_admin import urls as superadmin_urls
from bikers import urls as bikers_urls
from home import urls as home_urls



urlpatterns = [
    path('super_admin/', admin.site.urls),
    url(r'', include((home_urls,'home_urls' ) , namespace = 'homepage') ),
    url(r'maps/', include((map_urls,'map_urls' ) , namespace = 'maps') ),
    url(r'business/', include((business_urls,'business_urls' ) , namespace = 'business') ),
    url(r'accounts/', include((accounts_urls,'accounts_urls' ) , namespace = 'accounts') ),
    url(r'administrator/', include((superadmin_urls,'superadmin_urls' ) , namespace = 'superadmin_urls') ),
    url(r'bikers/', include((bikers_urls,'bikers_urls' ) , namespace = 'bikers') ),
]
# {% static 'main/images/img_avatar2.png' %}

# {% extends "layout.html" %}
# {% load static from staticfiles %}
# {% load bootstrap3 %}
# {% load leaflet_tags %}


# {% block head %}
# <style>
# /* Bordered form */
# form {
#   border: 3px solid #f1f1f1;
# }

# /* Full-width inputs */
# input[type=text], input[type=password] {
#   width: 100%;
#   padding: 12px 20px;
#   margin: 8px 0;
#   display: inline-block;
#   border: 1px solid #ccc;
#   box-sizing: border-box;
# }

# /* Set a style for all buttons */
# button {
#   background-color: #4CAF50;
#   color: white;
#   padding: 14px 20px;
#   margin: 8px 0;
#   border: none;
#   cursor: pointer;
#   width: 100%;
# }

# /* Add a hover effect for buttons */
# button:hover {
#   opacity: 0.8;
# }

# /* Extra style for the cancel button (red) */
# .cancelbtn {
#   width: auto;
#   padding: 10px 18px;
#   background-color: #f44336;
# }

# /* Center the avatar image inside this container */
# .imgcontainer {
#   text-align: center;
#   margin: 24px 0 12px 0;
# }

# /* Avatar image */
# img.avatar {
#   width: 40%;
#   border-radius: 50%;
# }

# /* Add padding to containers */
# .container {
#   padding: 16px;
# }

# /* The "Forgot password" text */
# span.psw {
#   float: right;
#   padding-top: 16px;
# }

# /* Change styles for span and cancel button on extra small screens */
# @media screen and (max-width: 300px) {
#   span.psw {
#     display: block;
#     float: none;
#   }
#   .cancelbtn {
#     width: 100%;
#   }
# }
# </style>

#     {% leaflet_js plugins="forms" %}
#     {% leaflet_css plugins="forms" %}
 
# {% endblock %}

# {% block content %}
# <div id="id01" class="modal">
#         <span onclick="document.getElementById('id01').style.display='none'" 
#       class="close" title="Close Modal">&times;</span>

# <form action="" method="POST">
#         <div class="imgcontainer">
#           <img src="img_avatar2.png" alt="Avatar" class="avatar">
#         </div>
      
#         <div class="container">
#             <h2>Sign Up {{type}}</h2>
#             {% bootstrap_form form %}
#             {% csrf_token %}
#             <input type="submit" value="Sign Up" class="btn btn-primary" >
#             <label>
#                 <input type="checkbox" checked="checked" name="remember"> Remember me
#             </label>
#         </div>
      
#         <div class="container" style="background-color:#f1f1f1">
#           <button type="button" class="cancelbtn">Cancel</button>
#           <span class="psw">Forgot <a href="#">password?</a></span>
#         </div>
#       </form>
# </div>
# {% endblock %}