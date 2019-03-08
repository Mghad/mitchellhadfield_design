from tethys_sdk.base import TethysAppBase, url_map_maker


class MitchellhadfieldDesign(TethysAppBase):
    """
    Tethys app class for Mitchellhadfield Design.
    """

    name = 'Mitchellhadfield Design'
    index = 'mitchellhadfield_design:home'
    icon = 'mitchellhadfield_design/images/Untitled-18-512.png'
    package = 'mitchellhadfield_design'
    root_url = 'mitchellhadfield-design'
    color = '#DA1EC6'
    description = 'Place a brief description of your app here.'
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
                url='mitchellhadfield-design',
                controller='mitchellhadfield_design.controllers.page'
            ),
        )

        return url_maps
