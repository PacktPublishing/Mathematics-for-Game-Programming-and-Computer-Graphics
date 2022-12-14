
### Get this product for $5

<i>Packt is having its biggest sale of the year. Get this eBook or any other book, video, or course that you like just for $5 each</i>


<b><p align='center'>[Buy now](https://packt.link/9781801077330)</p></b>


<b><p align='center'>[Buy similar titles for just $5](https://subscription.packtpub.com/search)</p></b>

# Mathematics for Game Programming and Computer Graphics

<a href="https://www.packtpub.com/product/mathematics-for-game-programming-and-computer-graphics/9781801077330"><img src="https://static.packt-cdn.com/products/9781801077330/cover/smaller" alt="Mathematics for Game Programming and Computer Graphics" height="256px" align="right"></a>

This is the code repository for [Mathematics for Game Programming and Computer Graphics](https://www.packtpub.com/product/mathematics-for-game-programming-and-computer-graphics/9781801077330), published by Packt.

**Explore the essential mathematics for creating, rendering, and manipulating 3D virtual environments**

## What is this book about?
Mathematics is an essential skill when it comes to graphics and game development, particularly if you want to understand the generation of real-time computer graphics and the manipulation of objects and environments in a detailed way. Python, together with Pygame and PyOpenGL, provides you the opportunity for to explore these features under the hood, revealing how computers generate and manipulate 3D environments.

This book covers the following exciting features: 
* Get up and running with Python, Pycharm, Pygame, and PyOpenGL
* Experiment with different graphics API drawing commands
* Review basic trigonometry and how it’s important in 3D environments
* Apply vectors and matrices to move, orient, and scale 3D objects
* Render 3D objects with textures, colors, shading, and lighting
* Work with vertex shaders for faster GPU-based rendering

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1801077339) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import pygame

pygame.init()
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, 
                 screen_height))

done = False
white = pygame.Color(255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 120, False, True)
text = font.render('Penny de Byl', False, white)
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  screen.blit(text, (10, 10))
  pygame.display.update()
pygame.quit()

```
Throughout the book, the code assumes the external files (models, textures and shaders) are in the same folder as the code accessing them.  However, in GitHub, the external files are accessed as if one folder higher.  Please keep this in mind for referencing external files in the code.
For example, if your project files are organized like this:
```
Root folder
- Project 1
---  Main.py
---  Models
------  Teapot.obj
```
It means that the models folder containing the teapot model is in the same folder as the main.py code.  To reference Teapot.obj from inside Main.py the address is:
“Models/Teapot.obj”
However, if you would like to keep the external files in one place and outside any particular chapter project you can place them on the same level as each chapter code (as is referenced in GitHub).  This structure appears as:
```
Root folder
     Project 1
------  Main.py
---  Models
------  Teapot.obj
```
In this case, the address of Teapot.obj should be:
“../Models/Teapot.obj”

The “../” in the file address tells the code to look up one folder from where the code is running from.

**Following is what you need for this book:**
This book is for programmers who want to enhance their 3D mathematics skills relating to computer graphics and computer games. Knowledge of high school–level mathematics and a working understanding in an object-orientated language is needed to grasp the contents present in this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-19).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-19        | Python                    | Windows, Mac OS X |
| 1-19     | Pygame           | Windows, Mac OS X |
| 1-19      | PyOpenGL          | Windows, Mac OS X |
| 1-19    | PyOpenGLOpenGL Shader Language (GLSL)           | Windows, Mac OS X |



We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/rmsvT).


### Related products <Other books you may enjoy>
* Game Physics Cookbook [[Packt]](https://www.packtpub.com/product/game-physics-cookbook/9781787123663) [[Amazon]](https://www.amazon.com/dp/1787123669)

* Applying Math with Python [[Packt]](https://www.packtpub.com/product/applying-math-with-python/9781838989750) [[Amazon]](https://www.amazon.com/dp/1838989757)

## Get to Know the Author
**Penny de Byl**
is a full stack developer with an honors in graphics and Ph.D. in artificial intelligence for games. She has a passion for teaching, teaching games development and computer graphics for over 25 years in universities in Australia and Europe. Her best-selling textbooks, including Holistic Game Development with Unity, are used in over 100 institutions. She has won numerous awards for teaching, including an Australian Government Excellence in Teaching Award and the Unity Mobile Game Curriculum Competition. Her approach to teaching computer science and related fields is project-based giving you hands-on workshops you can immediately get your teeth into. The full range of her teaching interests can be found at H3D Learn.





### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801077330">https://packt.link/free-ebook/9781801077330 </a> </p>