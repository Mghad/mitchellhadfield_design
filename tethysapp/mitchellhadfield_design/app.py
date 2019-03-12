from tethys_sdk.base import TethysAppBase, url_map_maker


class MitchellhadfieldDesign(TethysAppBase):
    """
    Tethys app class for Mitchellhadfield Design.
    """

    name = 'MitchellHadfield Design'
    index = 'mitchellhadfield_design:home'
    icon = 'mitchellhadfield_design/images/Untitled-18-512.png'
    package = 'mitchellhadfield_design'
    root_url = 'mitchellhadfield-design'
    color = '#DA1EC6'
    description = 'this app shows my wireframe mockup and proposal'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='mitchellhadfield-design',
                controller='mitchellhadfield_design.controllers.home'
            ),

            UrlMap(
                name='page',
                url='proposal',
                controller='mitchellhadfield_design.controllers.page'
            ),

            UrlMap(
                name='cheese',
                url='wireframes',
                controller='mitchellhadfield_design.controllers.cheese'
            ),
        )

        return url_maps
