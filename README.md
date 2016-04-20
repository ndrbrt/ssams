# SSAMS
## The 1KB cms

Ssams (Super Simple Articles Management System) is a very (veeery) minimalistic cms written in Python + Flask. It basically gives you an index page listing articles and a page to read them.

### Install and run

Be sure you have flask and markdown installed

  ```$ pip install flask```
  
  ```$ pip install markdown```

Download ssams, cd into ssams directory and

```$ python app.py```

### Usage

There is no login system, you won't need it. All you have to do is putting a Markdown formatted file into the `articles` folder and ssams will automatically detect it and it will be listed in the index view.

If you need to upload images for your articles just put them in the `static/images` folder and link to them in your Markdown code with `![Image Title](/static/images/image-file.jpg)`.

That's it.
