# How to setup a portfolio page on GitHub.io

In this tutorial, I will guide you through the process of quickly setting up your data science portfolio using Github Pages. Just a little bit of HTML, CSS and JS is all you need to get started. This is a great way to showcase your projects and share your work with the world.

The orignal idea I found [here](https://www.freedium.cfd/https://medium.com/@evanca/set-up-your-portfolio-website-in-less-than-10-minutes-with-github-pages-d0efa8ff56fd).

## Step 1: Create a new repository

Log in to your Github (or create an account if you don't have one at [github.com](https://github.com/join)) and create a new repository. Name it `username.github.io`, where `username` is your Github username. This will be the URL of your portfolio page.

## Step 2: Clone the repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

Create a new folder called `assets` and inside it create two folders called `css` and `js`.

## Step 3: Set up repository

Go to repository Settings and scroll down to "Pages” section. Under "Build and deployment" select `Deploy from a branch` under the “Source” and choose `master branch`.

## Step 4: Copy template files from my repository

Go to my [repository](https://github.com/TillMeineke/TillMeineke.github.io) and copy the respective files to the folders in your repository.

- `index.html`
- `/assets/css/style.css`
- `/assets/js/script.js`

Also copy needed images in the `/assets/images` folder or create your own.

## Step 5: Customize my template

Edit the `index.html` file to add your name, bio, and links to your projects. You can also customize the CSS and JS files to change the look and feel of your portfolio page. (The template is based on the templates from [here](https://dalum.vercel.app) and [here](https://daveebbelaar.github.io/)).

## Step 6: Push changes to the repository

Commit and push the changes to the repository using the following commands:

```bash
git add .
git commit -m "Initial commit"
git push origin master
```

## Step 7: Check your portfolio page

Magic Time 🎉

Your portfolio page should now be live at `https://username.github.io`.

Enjoy sharing your work with the world!

Please let me know if you have any questions or need help with setting up your portfolio page. I am happy to help.

I am looking for data science opportunities and would love to connect with you. You can find me on [LinkedIn](https://www.linkedin.com/in/tillmeineke/) and [github](https://github.com/TillMeineke).