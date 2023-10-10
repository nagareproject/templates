from nagare.server import application
from nagare import component, presentation


class {{context.project_name|capitalize}}:
    pass


@presentation.render_for({{context.project_name|capitalize}})
def render(self, h, *args):
    NAGARE = 'http://www.nagare.org/'
    NAGARE_DOC = NAGARE + 'doc/'

    this_file = __file__
    if this_file.endswith('.pyc'):
        this_file = __file__[:-1]

    h.head << h.head.title('Up and Running!')

    h.head.css_url('app.css')

    with h.div(id='body'):
        h << h.a(
            h.img(src='img/logo.png'),
            id='logo',
            href=NAGARE, title='Nagare home'
        )

        with h.div(id='content'):
            h << h.div('Congratulations!', id='title')

            with h.div(id='main'):
                h << h.h1('Your application is running')

                h << 'You can now add your application components into '
                h << h.em(this_file)
                h << ' or create new files'

                h << h.p(h.em('Have fun!'))

    with h.div(id='footer'):
        with h.table:
            with h.tr:
                h << h.th('About Nagare')
                h << h.th('Community')
                h << h.th('Learn', class_='last')

            with h.tr:
                with h.td:
                    with h.ul:
                        h << h.li(h.a('Description', href=NAGARE_DOC + 'description'))
                        h << h.li(h.a('Features', href=NAGARE_DOC + 'features'))
                        h << h.li(h.a('License', href=NAGARE_DOC + 'license'))

                with h.td:
                    with h.ul:
                        h << h.li(h.a('Github repositories', href='http://github.com/nagareproject'))
                        h << h.li(h.a('Mailing list', href='http://groups.google.com/group/nagare-users'))
                        h << h.li(h.a('Bugs report', href='https://github.com/nagareproject/core/issues'))

                with h.td(class_='last'):
                    with h.ul:
                        h << h.li(h.a('Documentation', href=NAGARE_DOC))
                        h << h.li(h.a('Demonstrations portal', href=NAGARE + 'portal'))
                        h << h.li(h.a('Demonstrations', href=NAGARE + 'demo'))
                        h << h.li(h.a('Wiki Tutorial', href=NAGARE + 'wiki'))

# ---------------------------------------------------------------


class App(application.App):

    def create_root(self):
        return component.Component({{context.project_name|capitalize}}())
