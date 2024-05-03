from datetime import date

from django.shortcuts import render

all_posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Alex",
    "date": date(2024, 5, 3),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was wnjoying the view!",
    "content": """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras dapibus lorem in mauris molestie elementum. Suspendisse sollicitudin magna vitae diam accumsan, sed pellentesque elit ultrices. Quisque nec nisl ut diam congue fermentum. Vestibulum id blandit sapien. Ut pharetra urna nisi, sed semper ante ornare quis. Curabitur in nibh odio. Proin ut nisl ut magna cursus volutpat. Mauris nec est pulvinar, tincidunt quam at, tincidunt diam.
      Pellentesque eget porttitor quam, dignissim imperdiet mi. Sed in dignissim justo. Cras egestas imperdiet dolor vel lobortis. Praesent vestibulum erat in odio elementum porttitor. Sed eget euismod mauris, sed placerat elit. Nulla auctor, arcu nec iaculis porttitor, nulla nulla semper diam, at semper odio dolor quis arcu. Nulla eros eros, cursus ut ex at, bibendum dictum massa. Praesent nec dolor eget dui egestas blandit. Ut ac magna tortor. Fusce congue, ipsum quis egestas volutpat, velit dui lobortis quam, non mattis metus ante sit amet justo.
      Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum vehicula est at pharetra venenatis. In eleifend justo lectus. Nullam pharetra volutpat dignissim. Mauris imperdiet augue ligula, sollicitudin rhoncus enim vestibulum a. Suspendisse vel euismod odio, sed euismod mi. Quisque vitae ipsum massa. Sed pretium venenatis tellus sit amet faucibus. Suspendisse efficitur risus et ex varius lobortis vitae eu ante. Mauris congue, tellus vel rhoncus vestibulum, ex tellus semper orci, et porttitor massa est a elit.
    """
  },
  {
    "slug": "programming-is-fun",
    "image": "coding.webp",
    "author": "Maximilian",
    "date": date(2022, 3, 10),
    "title": "Programming Is Great!",
    "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    "content": """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras dapibus lorem in mauris molestie elementum. Suspendisse sollicitudin magna vitae diam accumsan, sed pellentesque elit ultrices. Quisque nec nisl ut diam congue fermentum. Vestibulum id blandit sapien. Ut pharetra urna nisi, sed semper ante ornare quis. Curabitur in nibh odio. Proin ut nisl ut magna cursus volutpat. Mauris nec est pulvinar, tincidunt quam at, tincidunt diam.
      Pellentesque eget porttitor quam, dignissim imperdiet mi. Sed in dignissim justo. Cras egestas imperdiet dolor vel lobortis. Praesent vestibulum erat in odio elementum porttitor. Sed eget euismod mauris, sed placerat elit. Nulla auctor, arcu nec iaculis porttitor, nulla nulla semper diam, at semper odio dolor quis arcu. Nulla eros eros, cursus ut ex at, bibendum dictum massa. Praesent nec dolor eget dui egestas blandit. Ut ac magna tortor. Fusce congue, ipsum quis egestas volutpat, velit dui lobortis quam, non mattis metus ante sit amet justo.
      Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum vehicula est at pharetra venenatis. In eleifend justo lectus. Nullam pharetra volutpat dignissim. Mauris imperdiet augue ligula, sollicitudin rhoncus enim vestibulum a. Suspendisse vel euismod odio, sed euismod mi. Quisque vitae ipsum massa. Sed pretium venenatis tellus sit amet faucibus. Suspendisse efficitur risus et ex varius lobortis vitae eu ante. Mauris congue, tellus vel rhoncus vestibulum, ex tellus semper orci, et porttitor massa est a elit.
    """
  },
  {
    "slug": "into-the-woods",
    "image": "woods.jpg",
    "author": "Maximilian",
    "date": date(2020, 8, 5),
    "title": "Nature At Its Best",
    "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    "content": """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras dapibus lorem in mauris molestie elementum. Suspendisse sollicitudin magna vitae diam accumsan, sed pellentesque elit ultrices. Quisque nec nisl ut diam congue fermentum. Vestibulum id blandit sapien. Ut pharetra urna nisi, sed semper ante ornare quis. Curabitur in nibh odio. Proin ut nisl ut magna cursus volutpat. Mauris nec est pulvinar, tincidunt quam at, tincidunt diam.
      Pellentesque eget porttitor quam, dignissim imperdiet mi. Sed in dignissim justo. Cras egestas imperdiet dolor vel lobortis. Praesent vestibulum erat in odio elementum porttitor. Sed eget euismod mauris, sed placerat elit. Nulla auctor, arcu nec iaculis porttitor, nulla nulla semper diam, at semper odio dolor quis arcu. Nulla eros eros, cursus ut ex at, bibendum dictum massa. Praesent nec dolor eget dui egestas blandit. Ut ac magna tortor. Fusce congue, ipsum quis egestas volutpat, velit dui lobortis quam, non mattis metus ante sit amet justo.
      Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum vehicula est at pharetra venenatis. In eleifend justo lectus. Nullam pharetra volutpat dignissim. Mauris imperdiet augue ligula, sollicitudin rhoncus enim vestibulum a. Suspendisse vel euismod odio, sed euismod mi. Quisque vitae ipsum massa. Sed pretium venenatis tellus sit amet faucibus. Suspendisse efficitur risus et ex varius lobortis vitae eu ante. Mauris congue, tellus vel rhoncus vestibulum, ex tellus semper orci, et porttitor massa est a elit.
    """
  }
]

def get_date(post):
  return post['date']

# Create your views here.

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, 'blog/index.html', {
    'posts': latest_posts
  })

def posts(request):
  return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
  return render(request, 'blog/post-detail.html')