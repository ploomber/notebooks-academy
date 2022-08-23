# 1. Introduction

## Notes

Jupyter notebooks are a fantastic tool: you can write some code and get immediate feedback. It makes data science a lot more enjoyable!

Yet, they have problems: they can get hard to manage, reproduce and test. 

That's why many teams only allow their use for prototyping but do not use it in production.

**This course will teach the practices and tools to use Jupyter notebooks as a tool for production work effectively.**

At Ploomber, we've helped dozens of companies deploy notebooks into production: from small startups to Fortune 100 companies, so you're in good hands.

Fun fact: this course is entirely developed from Jupyter!

### What you'll learn?

- Write [clean](https://github.com/ploomber/notebooks-academy/blob/main/website/lessons/01/code/notebook.ipynb) Jupyter notebooks
- [Version control](https://github.com/ploomber/notebooks-academy/blob/main/website/lessons/01/code/notebook.py)
- Testing ([unit](https://github.com/ploomber/notebooks-academy/blob/main/website/lessons/01/code/test_notebook.py), integration)
- [Debugging](https://github.com/ploomber/notebooks-academy/blob/main/website/lessons/01/code/debugging.ipynb)
- Build [data pipelines](https://github.com/ploomber/notebooks-academy/tree/main/website/lessons/01/code/pipeline) from Jupyter
- Cloud deployment


<div id="jupyterlab-div">
  <a href="https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fnotebooks-academy%26urlpath%3Dlab%252Ftree%252Fnotebooks-academy%252Fwebsite%252Flessons%252F01%252Fcode%26branch%3Dmain" id="open-in-jupyterlab">Open in JupyterLab</a>
</div>


### Preparing your environment

To ensure you can run all the examples and get all the packages we'll use, we highly recommend installing [miniconda.](https://docs.conda.io/en/latest/miniconda.html)

Ensure you're able to create a conda environment:

```sh
# create environment
conda create --name some-env python=3.10 --yes

# activate it
conda activate some-env
```

You can also use other tools such as venv, but some packages might be harder to install. Whatever tool you choose, feel free to request help in the #notebooks-academy channel in our [Slack](https://ploomber.io/community).

### Commands used in the lesson

Here are the commands that we used during the video lesson:

```sh
# get the code
git clone https://github.com/ploomber/notebooks-academy

# move to the folder with the code
cd notebooks-academy/website/lessons/01/code
```

Convert `.ipynb` to `.py`:

```sh
pip install jupytext
jupytext notebook.ipynb --to py:percent
```

Run unit tests:

```sh
pip install pytest
pytest test_notebook.py
```

Generate data pipeline:

```sh
pip install soorgeon

mkdir pipeline
cd pipeline

soorgeon refactor ../notebook.ipynb
```

### Get involved!

[Join our community](https://ploomber.io/community), and ask us anything in the `#notebooks-academy` channel. We'll be answering questions and getting feedback over there. Help us make this online course a success!

### Recommended material

- [Ploomber: Maintainable and Collaborative Pipelines in Jupyter](https://blog.jupyter.org/ploomber-maintainable-and-collaborative-pipelines-in-jupyter-acb3ad2101a7)
- [Why (and how) to put notebooks in production](https://ploomber.io/blog/nbs-production)
- [On the Myths and Problems of Jupyter Notebooks](https://ploomber.io/blog/nbs-myths/)
- [Evidation Health presentation at PyData Global 2021](https://www.youtube.com/watch?v=cFpUBiSgDwU)

## Don't miss a lesson

<div id="newsletter">
<div class="newsletter-copy"><b>Subscribe to get the lessons delivered as soon as they're out:</b></div>
<div id="revue-embed">
  <form action="https://www.getrevue.co/profile/ploomber/add_subscriber" method="post" id="revue-form" name="revue-form"  target="_blank">
  <div class="revue-form-group" id="email-text-field">
    <input class="revue-form-field" placeholder="Your email address" type="email" name="member[email]" id="member_email">
  </div>
  <div class="revue-form-actions" id="submit-btn">
    <input type="submit" value="Subscribe" name="member[subscribe]" id="member_submit">
  </div>
  </form>
</div>
</div>

