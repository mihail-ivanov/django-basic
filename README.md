## Synopsis

Simple Django project with configured [webpack](https://webpack.github.io/) for processing ReactJS compilation and [django-sass-processor](https://github.com/jrief/django-sass-processor) for processing SCSS compilation (included examples with Bootstrap 4 and Foundation Sites).

## Motivation

Reduce initial time required to configure a project from the start.

## Jinja2 support

Jinja2 support (instead of Django templates) is added in a separate branch 'jinja2'.

## Installation

Example installation steps:

1. Clone the project (if jinja2 is required: `git checkout jinja2`)
2. Rename 'django_basic' to the name of your project (for example: 'my_awesome_project')
3. `npm install`
4. `python manage.py rebuild_webpack`

## License

[MIT license](LICENSE)
