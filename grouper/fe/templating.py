from typing import NamedTuple, TYPE_CHECKING

from grouper.templating import BaseTemplateEngine

if TYPE_CHECKING:
    from grouper.fe.settings import FrontendSettings

# An external web resource with SRI.
ExternalResource = NamedTuple("ExternalResource", [("url", str), ("integrity", str)])

# External JavaScript loaded on every Grouper page.  All URLs are relative to a CDNJS mirror.
EXTERNAL_JS = [
    ExternalResource(
        url="/ajax/libs/jquery/2.1.1/jquery.min.js",
        integrity="sha256-wNQJi8izTG+Ho9dyOYiugSFKU6C7Sh1NNqZ2QPmO0Hk=",
    ),
    ExternalResource(
        url="/ajax/libs/lodash.js/2.4.1/lodash.min.js",
        integrity="sha256-gOpnA1vUitDpr6qV2ONTzFxXQKgnwvBCOklJH6hHqyE=",
    ),
    ExternalResource(
        url="/ajax/libs/twitter-bootstrap/3.1.1/js/bootstrap.min.js",
        integrity="sha256-iY0FoX8s/FEg3c26R6iFw3jAtGbzDwcA5QJ1fiS0A6E=",
    ),
    ExternalResource(
        url="/ajax/libs/moment.js/2.7.0/moment.min.js",
        integrity="sha256-FQODX4G5IRIuYRmkc+gFKbr7DXrrqFrPjZkLVJSDQZQ=",
    ),
    ExternalResource(
        url="/ajax/libs/datatables/1.10.10/js/jquery.dataTables.min.js",
        integrity="sha256-YKbJo9/cZwgjue3I4jsFKdE+oGkrSpqZz6voxlmn2Fo=",
    ),
    ExternalResource(
        url="/ajax/libs/bootstrap-datetimepicker/3.0.0/js/bootstrap-datetimepicker.min.js",
        integrity="sha256-8e6Htoin9PzZslStDJ7tnwZa9lIIaXCQy2sDOA2P6WI=",
    ),
    ExternalResource(
        url="/ajax/libs/chosen/1.4.2/chosen.jquery.min.js",
        integrity="sha256-nOTrbQXdTPaimxT0mqnbsQGNDis1wmMPxII8apvxt3I=",
    ),
]


class FrontendTemplateEngine(BaseTemplateEngine):
    """Frontend-specific template engine."""

    def __init__(self, settings, deployment_name):
        # type: (FrontendSettings, str) -> None
        super(FrontendTemplateEngine, self).__init__(settings, "grouper.fe")
        template_globals = {
            "cdnjs_prefix": settings.cdnjs_prefix,
            "deployment_name": deployment_name,
            "external_js": EXTERNAL_JS,
        }
        self.environment.globals.update(template_globals)
